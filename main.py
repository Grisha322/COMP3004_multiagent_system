from experiment import Experiment, ExperimentWithDistributedSystem, ExperimentWithSupervisedSystem

def runExperiments(numberOfBots: int, numberOfRuns: int, experimentType: int, numberOfMoves: int, numberOfDirt: int):
    if experimentType == 0:
        experiment = ExperimentWithSupervisedSystem()
        print("Experiment with supervised system")
    elif experimentType == 1:
        experiment = ExperimentWithDistributedSystem()
        print("Experiment with distributed system")
    else:
        experiment = Experiment()
        print("Experiment with baseline system")

    print(f"Number of bots: %d" % numberOfBots)
    avgScore = 0
    avgDirtCollected = 0
    avgPercentageOfDirtCollected = 0
    avgExistanceOfPriorityArea = 0
    for i in range(0, numberOfRuns):
        counter = experiment.run(numberOfMoves, numberOfDirt, numberOfBots)
        score = counter.score
        dirtCollected = counter.totalDirtAddedNumber - counter.uncollectedDirtNumber
        percentageOfDirtCollected = (counter.totalDirtAddedNumber - counter.uncollectedDirtNumber) / counter.totalDirtAddedNumber * 100
        existanceOfPriorityArea = counter.existanceOfPriorityAreas / numberOfMoves * 100
        print(f"%.2f %d %.2f %.2f" % (score, dirtCollected, \
        percentageOfDirtCollected, existanceOfPriorityArea))

        avgScore += score
        avgDirtCollected += dirtCollected
        avgPercentageOfDirtCollected += percentageOfDirtCollected
        avgExistanceOfPriorityArea += existanceOfPriorityArea

    avgScore /= numberOfRuns
    avgDirtCollected /= numberOfRuns
    avgPercentageOfDirtCollected /= numberOfRuns
    avgExistanceOfPriorityArea /= numberOfRuns

    print(f"Average results of experiments: %.2f %d %.2f %.2f" % (avgScore, avgDirtCollected, avgPercentageOfDirtCollected, avgExistanceOfPriorityArea))

def main():
    numberOfRuns = 10
    numberOfBots = [2, 4, 8, 10] # only 2 4 8 and 10 are supported, check out readme for more info
    numberOfMoves = [1000, 1000, 1000, 1000]
    numberOfDirt = [2000, 3000, 4000, 5000]
    for idx, n in enumerate(numberOfBots):
        runExperiments(n, numberOfRuns, 0, numberOfMoves[idx], numberOfDirt[idx])
        runExperiments(n, numberOfRuns, 1, numberOfMoves[idx], numberOfDirt[idx])
        runExperiments(n, numberOfRuns, 2, numberOfMoves[idx], numberOfDirt[idx])
        
main()