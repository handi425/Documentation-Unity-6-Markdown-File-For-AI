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

#
[IPostBuildPlayerScriptDLLs](Build.IPostBuildPlayerScriptDLLs.html).OnPostBuildPlayerScriptDLLs

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

public void
OnPostBuildPlayerScriptDLLs([Build.Reporting.BuildReport](Build.Reporting.BuildReport.html)
report);

### Parameters

report | A report containing information about the build, such as its target platform and output path.  
---|---  
  
### Description

Implement this interface to receive a callback just after the player scripts
have been compiled.

You can implement this if you need to read or patch managed Assemblies for
players being built. You can get assembly locations from the
[files](BuildReport.files.html) property of the `report` parameter. Note that
implementing this callback will cause builds to run slower, as assemblies need
to be copied to an intermediate location, and is not recommended for best
performance.  
  
Additional resources: [BuildPlayerProcessor](Build.BuildPlayerProcessor.html),
[IFilterBuildAssemblies](Build.IFilterBuildAssemblies.html),
[IUnityLinkerProcessor](Build.IUnityLinkerProcessor.html),
[IPreprocessBuildWithReport](Build.IPreprocessBuildWithReport.html)

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Build;
    using UnityEditor.Build.Reporting;
    using UnityEngine;  
      
    class MyCustomBuildProcessor : [IPostBuildPlayerScriptDLLs](Build.IPostBuildPlayerScriptDLLs.html)
    {
        public int callbackOrder { get { return 0; } }
        public void OnPostBuildPlayerScriptDLLs([BuildReport](Build.Reporting.BuildReport.html) report)
        {
            [Debug.Log](Debug.Log.html)("MyCustomBuildProcessor.OnPostBuildPlayerScriptDLLs for target " + report.summary.platform + " at path " + report.summary.outputPath);
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

