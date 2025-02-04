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

#  [PBXProject](iOS.Xcode.PBXProject.html).GetBaseReferenceForConfig

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

public string GetBaseReferenceForConfig(string configGuid);

### Parameters

configGuid | The GUID of the build configuration as returned by [BuildConfigByName](iOS.Xcode.PBXProject.BuildConfigByName.html).  
---|---  
  
### Returns

**string** The GUID of the configuration file being used as the base
reference.

### Description

Gets the base configuration reference GUID for the specified build
configuration.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.IO;
    using UnityEditor.Callbacks;
    using UnityEditor.iOS.Xcode;  
      
    public class Sample_GetBaseReferenceForConfig  
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
            
            // Get the main target GUID
            string mainTargetGuid = pbxProject.GetUnityMainTargetGuid();  
      
            // Retrieve the configuration name (this can be "[Debug](Debug.html)", "Release", or any custom configuration name)
            string configName = "[Debug](Debug.html)";  
      
            // Get the "[Debug](Debug.html)" build configuration GUID 
            string configGuid = pbxProject.BuildConfigByName(mainTargetGuid, configName);
            
            // Use GetBaseReferenceForConfig to get the base reference for the specified configuration
            string baseReference = pbxProject.GetBaseReferenceForConfig(configGuid);  
      
            // Check if baseReference for specified configuration was found
            if (string.IsNullOrEmpty(baseReference))
            {
                [Debug.LogError](Debug.LogError.html)("Unable to find base reference for build configuration: " + configName);
                return;
            }
            else
            {
                // Modify the project using baseReference here
                // In this example we just print the baseReference for "[Debug](Debug.html)" config in Console
                [Debug.Log](Debug.Log.html)($"Base reference for {configName} configuration is: {baseReference}");
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

