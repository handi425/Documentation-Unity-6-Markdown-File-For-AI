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

#  [PBXProject](iOS.Xcode.PBXProject.html).AddFrameworkToProject

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

public void AddFrameworkToProject(string targetGuid, string framework, bool
weak);

### Parameters

targetGuid | The GUID of the build configuration as returned by [TargetGuidByName](iOS.Xcode.PBXProject.TargetGuidByName.html).  
---|---  
framework | The name of the framework. The extension of the filename must be `.framework`.  
weak | True if the framework is optional, for example if it's weakly linked, and false if the framework is required.  
  
### Description

Adds a system framework dependency for the specified target.

The function assumes system frameworks are located in the
`System/Library/Frameworks`folder in the SDK source tree. The framework is
added to Frameworks logical folder in the project.

    
    
    using System.IO;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.iOS.Xcode;
    using UnityEditor.Callbacks;
    using System.Collections;  
      
    public class Sample_AddFrameworkToProject
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
      
            // Get GUIDs for UnityFramework and Main targets
            string unityFrameworkTargetGuid = pbxProject.GetUnityFrameworkTargetGuid();
            string mainTargetGuid = pbxProject.GetUnityMainTargetGuid();  
      
            // Add a required framework to UnityFramework target 
            pbxProject.AddFrameworkToProject(unityFrameworkTargetGuid, "CoreBluetooth.framework", false);  
      
            // Add an optional framework to main target
            pbxProject.AddFrameworkToProject(mainTargetGuid, "MapKit.framework", true);  
      
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

