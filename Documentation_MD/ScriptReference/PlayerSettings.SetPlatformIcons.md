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

#  [PlayerSettings](PlayerSettings.html).SetPlatformIcons

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

## Declaration

public static void
SetPlatformIcons([Build.NamedBuildTarget](Build.NamedBuildTarget.html)
buildTarget, [PlatformIconKind](PlatformIconKind.html) kind, PlatformIcon[]
icons);

**Obsolete** Use SetPlatformIcons(NamedBuildTarget , PlatformIconKind)
instead.

## Declaration

public static void SetPlatformIcons([BuildTargetGroup](BuildTargetGroup.html)
platform, [PlatformIconKind](PlatformIconKind.html) kind, PlatformIcon[]
icons);

### Parameters

platform | The full list of platforms that support this API the supported kinds can be found in [icon kinds](PlatformIconKind.html).  
---|---  
icons | All available [PlatformIcon](PlatformIcon.html) slots must be retrieved with GetPlatformIcons.  
buildTarget | The [NamedBuildTarget](Build.NamedBuildTarget.html).  
  
### Description

Assign a list of icons for the specified platform and icon kind.

Most platforms support icons with several different sizes. This methods allows
you to set [Icons](PlatformIcon.html) for each platform that supports them.
GetPlatformIcons has to be used to retrieve all the supported icons for
specified [PlatformIconKind](PlatformIconKind.html) and platform. Texture
files must be stored in the project and instances obtained using
[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html).  
  
BuildTargetGroup is marked for deprecation in the future. Use
[NamedBuildTarget](Build.NamedBuildTarget.html) instead.  
  
The following code sample shows how to set up adaptive icons for an Android
application. This is an editor script which means it must be within an Editor
folder to compile.

    
    
    using UnityEditor.Android;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.Build;  
      
    public static class AndroidPlayerSettingsUtility
    {
        // `Adaptive` icons for [Android](PlayerSettings.Android.html) require a background and foreground layer for each icon
        public static void SetIcons([Texture2D](Texture2D.html)[][] textures)
        {
            [NamedBuildTarget](Build.NamedBuildTarget.html) platform = [NamedBuildTarget.Android](Build.NamedBuildTarget.Android.html);
            [PlatformIconKind](PlatformIconKind.html) kind = [AndroidPlatformIconKind.Adaptive](Android.AndroidPlatformIconKind.Adaptive.html);  
      
            [PlatformIcon](PlatformIcon.html)[] icons = [PlayerSettings.GetPlatformIcons](PlayerSettings.GetPlatformIcons.html)(platform, kind);  
      
            //Assign textures to each available icon slot.
            for (int i = 0; i < icons.Length; i++)
            {
                icons[i].SetTextures(textures[i]);
            }
            [PlayerSettings.SetPlatformIcons](PlayerSettings.SetPlatformIcons.html)(platform, kind, icons);
        }
    }
    

The following code sample shows how to set all App icons for an iOS
application. This is an editor script which means it must be within an Editor
folder to compile.

    
    
    using UnityEditor.iOS;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.Build;  
      
    public static class iOSPlayerSettingsUtility
    {
        // Setting all `App` icons for [iOS](PlayerSettings.iOS.html)
        public static void SetAppIcons([Texture2D](Texture2D.html)[] textures)
        {
            [NamedBuildTarget](Build.NamedBuildTarget.html) platform = [NamedBuildTarget.iOS](Build.NamedBuildTarget.iOS.html);
            [PlatformIconKind](PlatformIconKind.html) kind = [iOSPlatformIconKind.Application](iOS.iOSPlatformIconKind.Application.html);  
      
            [PlatformIcon](PlatformIcon.html)[] icons = [PlayerSettings.GetPlatformIcons](PlayerSettings.GetPlatformIcons.html)(platform, kind);  
      
            //Assign textures to each available icon slot.
            for (int i = 0; i < icons.Length; i++)
            {
                icons[i].SetTextures(textures[i]);
            }
            [PlayerSettings.SetPlatformIcons](PlayerSettings.SetPlatformIcons.html)(platform, kind, icons);
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

