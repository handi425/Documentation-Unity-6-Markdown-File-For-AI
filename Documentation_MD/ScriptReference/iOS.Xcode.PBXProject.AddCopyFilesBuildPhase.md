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

#  [PBXProject](iOS.Xcode.PBXProject.html).AddCopyFilesBuildPhase

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

public string AddCopyFilesBuildPhase(string targetGuid, string name, string
dstPath, string subfolderSpec);

### Parameters

targetGuid | The GUID of the target, such as the one returned by [GetUnityFrameworkTargetGuid](iOS.Xcode.PBXProject.GetUnityFrameworkTargetGuid.html).  
---|---  
name | The name of the phase.  
dstPath | The destination path.  
subfolderSpec | The subfolder spec. The following usages are known: 

  * `10` for embedding frameworks.
  * `13` for embedding app extension content.
  * `16` for embedding watch content.

  
  
### Returns

**string** Returns the GUID of the new phase.

### Description

Creates a new **Copy Files** build phase for a given target.

If a **Copy Files** build phase with the same name, `dstPath`, and
`subfolderSpec` is already configured for the target, the function returns the
existing phase. The new phase is placed at the end of the list of build phases
configured for the target.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.iOS.Xcode;
    using UnityEditor.Callbacks;
    using System.IO;  
      
    public class Sample_AddCopyFilesBuildPhase  
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
      
            // Get main target GUID
            string mainTargetGuid = pbxProject.GetUnityMainTargetGuid();  
      
            // Add a Copy Files Build Phase to the main target
            pbxProject.AddCopyFilesBuildPhase(mainTargetGuid, "ExamplePhase", "path/to/file", "10");  
      
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

