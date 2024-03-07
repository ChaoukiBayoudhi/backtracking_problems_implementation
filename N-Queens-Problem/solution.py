class NQueensProblem:
    def __init__(self, n):
        self.n = n
        #list of all possible solutions
        #each solution is a list of column indexes
        self.result = []
    def valid_position(self,candidate_solution):
        row_index=len(candidate_solution)-1
        ok=True
        i=0
        while i<row_index and ok:
            diff=abs(candidate_solution[row_index]-candidate_solution[i])
            if diff==0 or diff==row_index-i:
                ok=False
            i+=1
        return ok
    def backtrack_solution(self,candidate_solution=[]):
        if len(candidate_solution)==self.n:
            #add the solution to the result list
            #we need to create a new list because the candidate_solution
            #is a reference and it will be modified in the next iterations
            self.result.append(list(candidate_solution))
        else:
            for i in range(self.n):
                #add the candidate column position to the solution
                candidate_solution.append(i)
                if self.valid_position(candidate_solution):
                    #go to the next row
                    #this is managed by the candidate_solution length
                    self.backtrack_solution(candidate_solution)
                candidate_solution.pop()
                #or
                #del candidate_solution[-1]

#testing
n=int(input("Enter the number of queens :"))
n_queens=NQueensProblem(n)
print(n_queens.result)
n_queens.backtrack_solution()
print("There is %d solutions for %d queens "%(len(n_queens.result),n))
for solution in n_queens.result:
    print(solution)
