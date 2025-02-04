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

#  [PBXProject](iOS.Xcode.PBXProject.html).GetCopyFilesBuildPhaseByTarget

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

public string GetCopyFilesBuildPhaseByTarget(string targetGuid, string name,
string dstPath, string subfolderSpec);

### Parameters

targetGuid | The GUID of the target, such as the one returned by [TargetGuidByName](iOS.Xcode.PBXProject.TargetGuidByName.html).  
---|---  
name | The name of the phase.  
dstPath | The destination path.  
subfolderSpec | The subfolder spec. The following usages are known: 

  * `10` for embedding frameworks.
  * `13` for embedding app extension content.
  * `16` for embedding watch content.

  
  
### Returns

**string** Returns the GUID of the matching phase or null if it does not
exist.

### Description

Returns the GUID of matching copy files build phase for the given target.

The parameters of existing copy files build phase are matched to the arguments
of this function and the GUID of the phase is returned only if a matching
build phase is found.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.IO;
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;
    using UnityEditor.iOS.Xcode.Extensions;  
      
    public class Sample_GetCopyFilesBuildPhaseByTarget  
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
      
            // Get the "Embed Frameworks" build phase GUID 
            string copyFilesPhase = pbxProject.GetCopyFilesBuildPhaseByTarget(targetGuid, "Embed Frameworks", "", "10");  
      
            // Log the "Embed Frameworks" build phase GUID for debugging
            [Debug.Log](Debug.Log.html)("Copy 'Embed Frameworks' phase GUID: " + copyFilesPhase);
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

