from FunctionsReinsert import *
import sys

if __name__ == "__main__":
    
    blockDesc = sys.argv[1]
    
    
    helper = FunctionsReinsert()
    
    if blockDesc != "All":
        
        slpsName = sys.argv[2]
        print("\nWhat's inside this block :")
        helper.showSections(blockDesc)
        
        print("Create the script based on google sheet")
        helper.createAtlasScript_Block(blockDesc)
        
        
        print("Create the SLPS for this block")
        helper.reinsertText_Block(blockDesc, slpsName)
    else:
        
        helper.createAtlasScript_All()
        
        print("Create the SLPS for this block")
        helper.reinsertText_All()