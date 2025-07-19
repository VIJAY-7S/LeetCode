class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        truefolder=[]
        truefolder.append(folder[0])
        for i in folder:
            if i.startswith(truefolder[-1]+"/"):
                continue
            else:
                truefolder.append(i)
        return truefolder[1:]