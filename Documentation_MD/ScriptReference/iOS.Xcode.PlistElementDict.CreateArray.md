[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [PlistElementDict](iOS.Xcode.PlistElementDict.html).CreateArray

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public [iOS.Xcode.PlistElementArray](iOS.Xcode.PlistElementArray.html)
CreateArray(string key);

### Parameters

key | The key of the property.  
---|---  
  
### Returns

**PlistElementArray** The new array element.

### Description

Convenience method to set a property to a new array element.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class PlistCreateArrayExample
    {
        [PostProcessBuild]
        public static void CreateArrayExample([BuildTarget](BuildTarget.html) buildTarget, string pathToBuiltProject)
        {
            if (buildTarget == [BuildTarget.iOS](BuildTarget.iOS.html)) 
            {
                // Read the contents of the Info.plist file that was generated during the build
                string plistPath = pathToBuiltProject + "/Info.plist";
                [PlistDocument](iOS.Xcode.PlistDocument.html) plist = new [PlistDocument](iOS.Xcode.PlistDocument.html)();
                plist.ReadFromFile(plistPath);
           
                // Get root plist element
                [PlistElementDict](iOS.Xcode.PlistElementDict.html) rootDict = plist.root;  
      
                // Use CreateArray to create a new array entry called "AdditionalInfo" in the Info.plist file
                rootDict.CreateArray("AdditionalInfo");
                
                // Get the reference to the newly created "AdditionalInfo" array
                var array = rootDict["AdditionalInfo"].AsArray();
                
                // Use helper methods such as AddString, AddInteger or AddBoolean to add new values to the array
                array.AddString("PluginInfo");
                array.AddString("Disabled");
                array.AddInteger(75);
                array.AddBoolean(false);
                
                // Write the changes to the Info.plist file
                plist.WriteToFile(plistPath);
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

