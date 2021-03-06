'''
Problem Statement
        
You have decided to organize a grassroots campaign for world peace. Your plan is to assign ordinary citizens into groups of k penpals such that each group contains citizens from k different countries. People in each group will exchange letters in an effort to increase their understanding of each other's cultures. Given k and the populations of the participating countries as a int[] countries, you must determine the maximum number of groups that can be formed.

Note that no individual may be assigned to more than one group, and that some individuals may be left without a group.

 
Definition
        
Class:    WorldPeace
Method:    numGroups
Parameters:    int, int[]
Returns:    long
Method signature:    long numGroups(int k, int[] countries)
(be sure your method is public)
    
 
Constraints
-    k is between 2 and 20, inclusive.
-    countries contains between k and 50 elements, inclusive.
-    Each element of countries is between 1 and 1000000000 (one billion), inclusive.
 
Examples
0)    
        
4
{ 4,4,4,4,4 }
Returns: 5
Suppose the countries are Canada, China, Poland, Sweden, and the USA. Then you can make 5 groups as follows:
     Canada, China,  Poland, Sweden
     Canada, China,  Poland, USA
     Canada, China,  Sweden, USA
     Canada, Poland, Sweden, USA
     China,  Poland, Sweden, USA
1)    
        
5
{ 1,2,3,4,5,6 }
Returns: 3
Suppose the countries are designated 1 through 6, according to population. Then three groups are possible:
   2,3,4,5,6
   2,3,4,5,6
   1,3,4,5,6
There are six people left unassigned, but they come from only three different countries, so they cannot be made into another group.
2)    
        
2
{ 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000 }
Returns: 3000000000
3)    
        
7
{ 96, 17, 32, 138, 112, 50, 7, 19, 412, 23, 14, 50, 47, 343, 427, 22, 39 }
Returns: 166
4)    
        
10
{ 638074479, 717901019, 910893151, 924124222, 991874870, 919392444, 729973192, 607898881, 
  838529741, 907090878, 632877562, 678638852, 749258866, 949661738, 784641190, 815740520, 
  689809286, 711327114, 658017649, 636727234, 871088534, 964608547, 867960437, 964911023, 
  642411618, 868318236, 793328473, 849540177, 960039699, 998262224, 775720601, 634685437, 
  743766982, 826321850, 846671921, 712570181, 676890302, 814283264, 958273130, 899003369, 
  909973864, 921987721, 978601888, 633027021, 896400011, 725078407, 662183572, 629843174, 
  617774786, 695823011 }
Returns: 3983180234
'''
import unittest

class WorldPeace:
    def numGroups(self, k, countries):
        groups = 0
        minim = 0
        ccountries = countries[:] #make a slice copy of the provided list
        while True:
            ccountries.sort()
            ccountries.reverse()
            
            minim = ccountries[k-1]
            if (minim > 0):
                groups = groups + 1
                for i in range(k):
                    ccountries[i] = ccountries[i] -1
            else:
                break
        return groups; 
    

class WorldPeaceUnitTest(unittest.TestCase):
    def test_numGroups1(self):
        wp = WorldPeace()
        self.assertEqual(5, wp.numGroups(4, [4,4,4,4,4]))           
        
    def test_numGroups2(self):
        wp = WorldPeace()
        self.assertEquals(3, wp.numGroups(5, [1,2,3,4,5,6]))
        
    def test_numGroups3(self):
        wp = WorldPeace()            
        self.assertEquals(166, wp.numGroups(7, [ 96, 17, 32, 138, 112, 50, 7, 19, 412, 23, 14, 50, 47, 343, 427, 22, 39]))            

