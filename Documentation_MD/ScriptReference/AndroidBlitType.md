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

# AndroidBlitType

enumeration

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

### Description

Describes the method for how content is displayed on the screen.

Options are as follows:  
  
Use **Always** to render offscreen and blit to the backbuffer. Use **Never**
to render directly to the backbuffer. Use **Auto** or automatically choose the
most appropriate option.  
  
Depending on the device, [AndroidBlitType.Never](AndroidBlitType.Never.html)
may not support switching MSAA settings at runtime or rendering at non-native
resolution. [AndroidBlitType.Never](AndroidBlitType.Never.html) does not
provide a sRGB backbuffer. Linear rendering requires a framebuffer that does
sRGB read/write conversions (see [RenderTexture.sRGB](RenderTexture-
sRGB.html)), otherwise the generated image typically appears too dark.
Therefore [AndroidBlitType.Never](AndroidBlitType.Never.html) is not
recommended when linear rendering is used. If you want to use linear rendering
with [AndroidBlitType.Never](AndroidBlitType.Never.html) despite this
information, you have to setup your own sRGB render target and handle the blit
to the backbuffer.  
  
AndroidBlitType is ignored when the Vulkan Graphics API is used.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Build;
    using UnityEngine;  
      
    public class AndroidBlitTypeExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Build/[Android](PlayerSettings.Android.html) Blit Type Auto Example")]
        public static void AndroidBlitTypes()
        {
            [PlayerSettings.SetScriptingBackend](PlayerSettings.SetScriptingBackend.html)([NamedBuildTarget.Android](Build.NamedBuildTarget.Android.html), [ScriptingImplementation.IL2CPP](ScriptingImplementation.IL2CPP.html));
            [PlayerSettings.Android.targetArchitectures](PlayerSettings.Android-targetArchitectures.html) = [AndroidArchitecture.ARM64](AndroidArchitecture.ARM64.html);  
      
            //Set [AndroidBlitType](AndroidBlitType.html) to Auto which automatically determines
            //the most appropriate method for drawing to the screen.
            [PlayerSettings.Android.blitType](PlayerSettings.Android-blitType.html) = [AndroidBlitType.Auto](AndroidBlitType.Auto.html);  
      
            [BuildPlayerOptions](BuildPlayerOptions.html) options = new [BuildPlayerOptions](BuildPlayerOptions.html)();
            options.scenes = new[] { "Assets/Scenes/SampleScene.unity" };
            options.locationPathName = "Builds/AndroidBuild.apk";
            options.target = [BuildTarget.Android](BuildTarget.Android.html);
            options.targetGroup = [BuildTargetGroup.Android](BuildTargetGroup.Android.html);  
      
            [BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html)(options);
        }
    }

### Properties

[Always](AndroidBlitType.Always.html)| Always render offscreen and blit to the
backbuffer.  
---|---  
[Never](AndroidBlitType.Never.html)| Never render offscreen and blit to the
backbuffer. Always render directly to the backbuffer.  
[Auto](AndroidBlitType.Auto.html)| Automatically determine the most
appropriate method for drawing to the screen.  
  
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

