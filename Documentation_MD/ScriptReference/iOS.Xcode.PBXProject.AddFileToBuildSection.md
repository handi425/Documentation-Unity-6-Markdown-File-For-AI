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

#  [PBXProject](iOS.Xcode.PBXProject.html).AddFileToBuildSection

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

public void AddFileToBuildSection(string targetGuid, string sectionGuid,
string fileGuid);

### Parameters

targetGuid | The GUID of the target, such as the one returned by [TargetGuidByName](iOS.Xcode.PBXProject.TargetGuidByName.html).  
---|---  
sectionGuid | The GUID of the section to add the file to.  
fileGuid | The file GUID returned by [AddFile](iOS.Xcode.PBXProject.AddFile.html) or [AddFolderReference](iOS.Xcode.PBXProject.AddFolderReference.html).  
  
### Description

Configures file for building for the given native target on specific build
section.

The function is equivalent to
[AddFileToBuild](iOS.Xcode.PBXProject.AddFileToBuild.html) except that a
specific build section is defined. In projects containing multiple native
targets, you can configure a single file or folder reference to build in all,
some, or none of the targets. The file or folder reference is added to
appropriate build section depending on the file extension.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.IO;
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class Sample_AddFileToBuildSection  
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
      
            // Get GUID for Main target
            string mainTargetGuid = pbxProject.GetUnityMainTargetGuid();  
      
            // Specify the file path you want to add to the Xcode project
            string filePath = Path.Combine([Application.dataPath](Application-dataPath.html), "[Resources](Resources.html)/InputFile.txt");  
      
            // Add the file to '[Resources](Resources.html)' subfolder in the Xcode project
            string fileGuid = pbxProject.AddFile(filePath, "[Resources](Resources.html)/InputFile.txt");  
      
            // Get a GUID for the section you want to add the file to
            string resourcePhaseGuid = pbxProject.GetSourcesBuildPhaseByTarget(mainTargetGuid);  
      
            // Add the file to build by specifying the section GUID
            pbxProject.AddFileToBuildSection(mainTargetGuid, resourcePhaseGuid, fileGuid);  
      
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

