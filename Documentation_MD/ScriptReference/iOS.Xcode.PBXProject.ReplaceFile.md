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

#  [PBXProject](iOS.Xcode.PBXProject.html).ReplaceFile

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

public void ReplaceFile(string fileGuid, string path,
[iOS.Xcode.PBXSourceTree](iOS.Xcode.PBXSourceTree.html) source);

### Parameters

fileGuid | The GUID of the file reference.  
---|---  
path | The physical path to the new file on the filesystem.  
source | The source tree the path is relative to. By default it's [PBXSourceTree.Source](iOS.Xcode.PBXSourceTree.Source.html). The [PBXSourceTree.Group](iOS.Xcode.PBXSourceTree.Group.html) tree is not supported.  
  
### Description

Replaces a specified file with a new file.

The path to the specified file is replaced and the GUID of the old file is
preserved.

    
    
    using [UnityEditor](UnityEditor.html);
    using System.IO;
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class Sample_ReplaceFile  
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
            string targetGuid = pbxProject.GetUnityMainTargetGuid();  
      
            // Get the GUID of the existing file you want to replace
            string existingFilePath = "[Resources](Resources.html)/oldExampleFile.txt";
            string existingFileGuid = pbxProject.FindFileGuidByProjectPath(existingFilePath);  
      
            // Add the new file and get the GUID
            string newFilePath = "path/to/your/newExampleFile.txt";
            string newFileGuid = pbxProject.AddFile(newFilePath, "[Resources](Resources.html)/newExampleFile.txt", [PBXSourceTree.Source](iOS.Xcode.PBXSourceTree.Source.html));  
      
            // Replace the existing file with the new file
            pbxProject.ReplaceFile(existingFileGuid, newFileGuid);
            
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

