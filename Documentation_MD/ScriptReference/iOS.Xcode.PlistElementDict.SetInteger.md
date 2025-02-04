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

#  [PlistElementDict](iOS.Xcode.PlistElementDict.html).SetInteger

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

public void SetInteger(string key, int val);

### Parameters

key | The key of the property.  
---|---  
val | The value of the property.  
  
### Description

Convenience method to set an integer property.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class PlistSetIntegerExample
    {
        [PostProcessBuild]
        public static void SetIntegerExample([BuildTarget](BuildTarget.html) buildTarget, string pathToBuiltProject)
        {
            if (buildTarget == [BuildTarget.iOS](BuildTarget.iOS.html)) 
            {
                // Read the contents of the Info.plist file that was generated during the build
                string plistPath = pathToBuiltProject + "/Info.plist";
                [PlistDocument](iOS.Xcode.PlistDocument.html) plist = new [PlistDocument](iOS.Xcode.PlistDocument.html)();
                plist.ReadFromFile(plistPath);
           
                // Get root plist element
                [PlistElementDict](iOS.Xcode.PlistElementDict.html) rootDict = plist.root;
                
                
                // Use SetInteger to change the value of "UIDeviceFamily" to "2"
                rootDict.SetInteger("UIDeviceFamily", 2);  
      
                // Use SetInteger to create a new Info.plist entry called "ExampleInteger" with "10" as the value
                // If a specified key doesn't already exist in the Info.plist, a new entry will be created
                rootDict.SetInteger("ExampleInteger", 10);  
      
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

