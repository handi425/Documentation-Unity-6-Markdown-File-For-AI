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
[EditorUserBuildSettings](EditorUserBuildSettings.html).SwitchActiveBuildTarget

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

**Obsolete** Please use SwitchActiveBuildTarget(BuildTargetGroup targetGroup,
BuildTarget target).

## Declaration

public static bool SwitchActiveBuildTarget([BuildTarget](BuildTarget.html)
target);

## Declaration

public static bool
SwitchActiveBuildTarget([BuildTargetGroup](BuildTargetGroup.html) targetGroup,
[BuildTarget](BuildTarget.html) target);

## Declaration

public static bool
SwitchActiveBuildTarget([Build.NamedBuildTarget](Build.NamedBuildTarget.html)
namedBuildTarget, [BuildTarget](BuildTarget.html) target);

### Parameters

target | Target build platform.  
---|---  
targetGroup | Build target group.  
namedBuildTarget | Target named build platform.  
  
### Returns

**bool** True if the build target was successfully switched, false otherwise
(for example, if license checks fail, files are missing, or if the user has
cancelled the operation via the UI).

### Description

Select a new build target to be active.

When changing the active build target, this function reimports Assets that are
affected by the current platform settings, and then returns true if the
operation completed successfully. All script files are compiled on the next
editor update. To have scripts compile before the Assets are reimported, refer
to
[SwitchActiveBuildTargetAsync](EditorUserBuildSettings.SwitchActiveBuildTargetAsync.html).  
  
If the given target is a standalone target, calling SwitchActiveBuildTarget
will also affect
[EditorUserBuildSettings.selectedStandaloneTarget](EditorUserBuildSettings-
selectedStandaloneTarget.html).  
  
**Note** : This method isn't available when running the Editor in [batch
mode](../Manual/EditorCommandLineArguments.html). Changing the build target
requires recompiling script code for the given target, which can't be done
while script code is executing. This isn't a problem in the Editor, as the
operation is deferred to the next Editor update. However, in batch mode the
Editor will stop after executing the designated script code, so deferring the
operation isn't possible. To set the build target to use in batch mode, use
the [buildtarget](../Manual/EditorCommandLineArguments.html) command-line
argument.

    
    
    using [UnityEditor](UnityEditor.html);  
      
    public class SwitchPlatformExample
    {
        [[MenuItem](MenuItem.html)("Example/[Switch](PlayerSettings.Switch.html) Platform")]
        public static void PerformSwitch()
        {
            // [Switch](PlayerSettings.Switch.html) to Windows standalone build.
            [EditorUserBuildSettings.SwitchActiveBuildTarget](EditorUserBuildSettings.SwitchActiveBuildTarget.html)([BuildTargetGroup.Standalone](BuildTargetGroup.Standalone.html), [BuildTarget.StandaloneWindows](BuildTarget.StandaloneWindows.html));
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

