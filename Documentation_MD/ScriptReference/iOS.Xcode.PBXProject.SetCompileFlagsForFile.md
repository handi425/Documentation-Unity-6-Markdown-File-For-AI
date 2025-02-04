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

#  [PBXProject](iOS.Xcode.PBXProject.html).SetCompileFlagsForFile

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

public void SetCompileFlagsForFile(string targetGuid, string fileGuid,
List<string> compileFlags);

### Parameters

targetGuid | The GUID of the target, such as the one returned by [TargetGuidByName](iOS.Xcode.PBXProject.TargetGuidByName.html).  
---|---  
fileGuid | The GUID of the file.  
compileFlags | The list of compile flags or null if the flags should be unset.  
  
### Description

Sets the compilation flags for the given file in the given target.

    
    
    using [UnityEditor](UnityEditor.html);
    using System.Collections.Generic;
    using System.IO;
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    public class Sample_SetCompileFlagsForFile  
    {
        [PostProcessBuild]
        public static void OnPostprocessBuild([BuildTarget](BuildTarget.html) buildTarget, string pathToBuiltProject)
        {  
      
            // Stop processing if build target is not [iOS](PlayerSettings.iOS.html)
            if (buildTarget != [BuildTarget.iOS](BuildTarget.iOS.html))
                return;  
      
            // Initialize [PBXProject](iOS.Xcode.PBXProject.html)
            string projectPath = [PBXProject.GetPBXProjectPath](iOS.Xcode.PBXProject.GetPBXProjectPath.html)(pathToBuiltProject);
            [PBXProject](iOS.Xcode.PBXProject.html) pbxProject = new [PBXProject](iOS.Xcode.PBXProject.html)();
            pbxProject.ReadFromFile(projectPath);  
      
            // Get the target GUID
            string targetGuid = pbxProject.GetUnityFrameworkTargetGuid();  
      
            // Specify the file path you want to get compile flags of (within the Xcode project)
            string filePath = "[Plugins](Unity.Android.Gradle.Plugins.html)/ExampleFile.mm";  
      
            // Retrieve the file GUID using the file path
            string fileGuid = pbxProject.FindFileGuidByProjectPath(filePath);  
      
            // Get the compile flags for the specified file
            string[] compileFlags = pbxProject.GetCompileFlagsForFile(targetGuid, fileGuid).ToArray();
            
            // Check if the file already has a compile flag you want to specify
            string customCompileFlag = "exampleFlag";
            if (Array.IndexOf(compileFlags, customCompileFlag) <  0)
            {
                // Add the compile flag if it doesn't
                pbxProject.SetCompileFlagsForFile(targetGuid, fileGuid, new List<string> (){customCompileFlag});
            }  
      
            // Apply changes to the pbxproj file
            pbxProject.WriteToFile(projectPath);
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

