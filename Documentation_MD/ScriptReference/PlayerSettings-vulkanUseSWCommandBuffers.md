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

**Method group is Obsolete**  

#  [PlayerSettings](PlayerSettings.html).vulkanUseSWCommandBuffers

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

**Obsolete** Vulkan SW command buffers are deprecated,
vulkanUseSWCommandBuffers will be ignored. public static bool
vulkanUseSWCommandBuffers;

### Description

Use software command buffers for building rendering commands on Vulkan.

If this setting is disabled, all rendering commands are built into secondary
command buffers, one per each graphics job. If enabled, all rendering commands
are instead serialized into a software buffer, and a separate thread is used
to build a single primary command buffer based on that information.  
  
Note: this setting is only intended to correct a specific issue when
displaying [IMGUI](../Manual/GUIScriptingGuide.html) in a project that uses
linear color space. If you are using IMGUI in a linear color space project,
your IMGUI graphics will be drawn incorrectly (their color will appear washed
out). This setting corrects that problem, but at a performance cost. On
desktop platforms this cost may not be noticable, but it is particularly
significant on mobile platforms with tile-based GPUs.  
  
The best way to avoid this issue, instead of enabling this setting, is to use
the [Canvas-based UI system](../Manual/UISystem.html) in your game instead of
IMGUI. IMGUI is not intended for in-game UI, it is mainly intended for
creating UI in the editor.

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

