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

#  [PBXProject](iOS.Xcode.PBXProject.html).SetBuildPropertyForConfig

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

public void SetBuildPropertyForConfig(string configGuid, string name, string
value);

## Declaration

public void SetBuildPropertyForConfig(IEnumerable<string> configGuids, string
name, string value);

### Parameters

configGuid | The GUID of the build configuration as returned by [BuildConfigByName](iOS.Xcode.PBXProject.BuildConfigByName.html).  
---|---  
configGuids | The GUIDs of the build configurations as returned by [BuildConfigByName](iOS.Xcode.PBXProject.BuildConfigByName.html).  
name | The name of the build property.  
value | The value of the build property.  
  
### Description

Sets a build property to the given value in the specified build
configuration(s).

Duplicate build properties are ignored. Values for names
`LIBRARY_SEARCH_PATHS` and `FRAMEWORK_SEARCH_PATHS` are quoted if they contain
spaces.

    
    
    using [UnityEditor](UnityEditor.html);
    using System.IO;
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class Sample_SetBuildPropertyForConfig  
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
      
            // Get the GUID you want to set a build property on
            string unityFrameworkTargetGuid = pbxProject.GetUnityFrameworkTargetGuid();  
      
            // Get the GUID of the "[Debug](Debug.html)" config so you can use it to change config-specific settings
            string configGuid = pbxProject.BuildConfigByName(unityFrameworkTargetGuid, "[Debug](Debug.html)");  
      
            // Set "ENABLE_BITCODE" to "NO" for "[Debug](Debug.html)" config 
            pbxProject.SetBuildPropertyForConfig(configGuid, "ENABLE_BITCODE", "NO");  
      
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

