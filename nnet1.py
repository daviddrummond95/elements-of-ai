import numpy as np
# this next package is only to monitor progress of epochs.
from tqdm import tqdm
import random
class NeuralNetwork:
    def __init__(self, x, y, w1, w2, alpha):
        self.input = x
        self.weights1 = w1
        self.weights2 =  w2
        self.y          = y
        self.alpha = alpha
        self.output     = np.array([[0],[0],[0],[0]])

    def sigmoid(self, x):
        return (1 / (1 + np.exp(-x)))

    def sigmoid_derivative(self, x):
        return x*(1-x)

    def feedforward(self):
        self.layer1 = self.sigmoid(np.dot(self.input, self.weights1))
        self.output = self.sigmoid(np.dot(self.layer1, self.weights2))
        return(self.output)

    # this was adapted from the article referenced in readme.
    def backprop(self):
        delta2 = self.alpha * np.dot(np.asmatrix(self.layer1).transpose(), np.asmatrix((self.y - self.output) * self.sigmoid_derivative(self.output)))
        delta1 = self.alpha * np.dot(np.asmatrix(self.input).transpose(),  np.asmatrix(np.dot((self.y - self.output) * self.sigmoid_derivative(self.output), self.weights2.T) * self.sigmoid_derivative(self.layer1)))
        return delta1, delta2



class trainandtest:
    def __init__(self, data, model):
        self.Datafile = data
        self.best = 0
        self.w1, self.w2 = self.open_model(model)
        self.hidden = 70
        self.PositionVector = ['0', '90', '180', '270']
        self.alpha = 0.0001
        self.epoch = 1000

    def open_file(self, file):
        with open(file, "r") as file:
            output = file.readlines()
        return output

    def open_model(self, file):

        model = open(file, 'r')
        output = model.readlines()
        self.best = float(output[0])
        w1 = []
        temp = []
        for i in output[1:]:
            if i == ';':
                break
            if i == '|\n':
                temp = ' '.join(temp); temp.replace('\n', '')
                temp = temp.split(' '); temp = list(filter(None, temp))
                w1.append(temp); temp = []
            else:
                i = i.replace('[', ''); i = i.replace(']', '')
                i = i.replace('\n', ' '); temp.append(i)
        for i in range(len(w1)):
            for j in range(len(w1[i])):
                w1[i][j] = float(w1[i][j])

        w2 = []
        check = False
        for i in output:
            if i == ";\n":
                check = True
                pass
            if not check:
                pass
            else:
                i = i.replace('[', '')
                i = i.replace(']', '')
                i = i.replace('\n', '')

                if i != ';':
                    i = i.split(' ')
                    i = list(filter(None, i))
                    w2.append(i)
        for i in range(len(w2)):
            for j in range(len(w2[i])):
                w2[i][j] = float(w2[i][j])
        w1 = np.array(w1)
        w2 = np.array(w2)
        return w1, w2
    def save_model(self, best, w1, w2):
        model = open('nnet_model.txt', 'w')
        model.write(str(best) + '\n')
        for i in w1:
            k = np.array2string(i)
            model.write(k)
            model.write('\n'+'|'+'\n')
        model.write(';'+ '\n')
        model.write(str(w2) + '\n')
        model.close()

    def predict(self, output):
        tempmax = -float('inf')
        tempmaxind = 0
        for i in range(len(output)):
            if output[i] > tempmax:
                tempmax = output[i]
                tempmaxind = i
        return tempmax, tempmaxind

    def yindex(self, array):
        for i in range(len(array)):
            if array[i] == 1:
                return i
    # this function was adapted from the code of a previous student. I added the ID vector part.
    # https://github.com/umangrmehta/image-orientation-classifier/blob/master/orient.py
    def createvector(self, data):
        with open(data, "r") as file:
            self.Data = file.readlines()
        DataLength = sum(1 for l in self.Data)
        inVector = np.zeros((DataLength, 192), dtype=np.int_)
        outVector = np.zeros((DataLength, 4), dtype=np.int8)
        idvector = []
        for lineNo, line in enumerate(self.Data):
            row = line[:-1].split(' ', 2)
            inVector[lineNo] = np.array(row[2].split(' '))
            outVector[lineNo, self.PositionVector.index(row[1])] = 1
            idvector.append(row[0])
        return inVector, outVector, DataLength, idvector

    def train(self):
        inputvector, outputvector, DataLength, idvector = self.createvector(self.Datafile)
        # the random weight function assignment and the vectorcheck ideas were learned from https://github.com/umangrmehta/image-orientation-classifier/blob/master/orient.py
        w1 = np.random.uniform(-1, 1, size=(192, self.hidden))
        w2 = np.random.uniform(-1, 1, size=(self.hidden, 4))
        for j in tqdm(range(self.epoch)):
            vectorCheck = np.zeros(DataLength, dtype=np.bool_)
            delta1total = 0
            delta2total = 0
            while not np.all(vectorCheck):
                i = random.randint(0, DataLength - 1)
                if vectorCheck[i]:
                    continue
                x = inputvector[i]
                y = outputvector[i]
                nn = NeuralNetwork(x, y, w1, w2, self.alpha)
                out = nn.feedforward()
                delta1, delta2 = nn.backprop()
                delta1total += delta1
                delta2total += delta2
                vectorCheck[i] = True
            w1 += delta1total
            w2 += delta2total
        truecount = 0
        falsecount = 0
        for i in range(DataLength):
            x = inputvector[i]
            y = outputvector[i]
            nn = NeuralNetwork(x, y, w1, w2, self.alpha)
            out = nn.feedforward()
            prediction, pindex = self.predict(out)
            index = self.yindex(y)

            if pindex == index:
                truecount += 1
            if pindex != index:
                falsecount += 1
        best = (truecount / (truecount + falsecount))
        print(best)
        if best > self.best:
            print(best)
            self.save_model(best, w1, w2)



    def test(self):
        testinVectors, testoutVectors, testLength, idvector = self.createvector(self.Datafile)
        truecount = 0
        falsecount = 0
        output = open('nnet_output.txt', 'w')
        output.write('')
        for i in range(1, testLength):
            x = testinVectors[i]
            y = testoutVectors[i]
            ID = idvector[i]
            w1 = self.w1
            w2 = self.w2
            nn = NeuralNetwork(x, y, w1, w2, self.alpha)
            out = nn.feedforward()
            prediction, pindex = self.predict(out)
            index = self.yindex(y)
            output = open('nnet_output.txt', 'a')
            output.write(ID+' '+ self.PositionVector[pindex]+ '\n')
            if pindex == index:
                truecount += 1
            if pindex != index:
                falsecount += 1
        print('Proportion predicted:', truecount/(truecount+falsecount))
