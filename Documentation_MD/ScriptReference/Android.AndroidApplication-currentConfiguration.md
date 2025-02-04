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

#  [AndroidApplication](Android.AndroidApplication.html).currentConfiguration

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

public static
[Android.AndroidConfiguration](Android.AndroidConfiguration.html)
currentConfiguration;

### Description

Provides current configuration for the running application.

Additional resources:
[AndroidApplication.onConfigurationChanged](Android.AndroidApplication-
onConfigurationChanged.html).

    
    
    using UnityEngine;
    using UnityEngine.Android;  
      
    public class ShowConfiguration : [MonoBehaviour](MonoBehaviour.html)
    {  
      
        public void Start()
        {
            var contents = new System.Text.StringBuilder();
            var c = [AndroidApplication.currentConfiguration](Android.AndroidApplication-currentConfiguration.html);
            contents.AppendLine($"* [ColorMode](Unity.Android.Gradle.Manifest.ColorMode.html), Hdr: {c.colorModeHdr}");
            contents.AppendLine($"* [ColorMode](Unity.Android.Gradle.Manifest.ColorMode.html), Gamut: {c.colorModeWideColorGamut}");
            contents.AppendLine($"* DensityDpi: {c.densityDpi}");
            contents.AppendLine($"* FontScale: {c.fontScale}");
            contents.AppendLine($"* FontWeightAdj: {c.fontWeightAdjustment}");
            contents.AppendLine($"* Keyboard: {c.keyboard}");
            contents.AppendLine($"* Keyboard Hidden, Hard: {c.hardKeyboardHidden}");
            contents.AppendLine($"* Keyboard Hidden, Normal: {c.keyboardHidden}");
            contents.AppendLine($"* Mcc: {c.mobileCountryCode}");
            contents.AppendLine($"* Mnc: {c.mobileNetworkCode}");
            contents.AppendLine($"* Navigation: {c.navigation}");
            contents.AppendLine($"* NavigationHidden: {c.navigationHidden}");
            contents.AppendLine($"* [Orientation](Tilemaps.Tilemap.Orientation.html): {c.orientation}");
            contents.AppendLine($"* ScreenHeightDp: {c.screenHeightDp}");
            contents.AppendLine($"* ScreenWidthDp: {c.screenWidthDp}");
            contents.AppendLine($"* SmallestScreenWidthDp: {c.smallestScreenWidthDp}");
            contents.AppendLine($"* ScreenLayout, [Direction](UIElements.NavigationMoveEvent.Direction.html): {c.screenLayoutDirection}");
            contents.AppendLine($"* ScreenLayout, Size: {c.screenLayoutSize}");
            contents.AppendLine($"* ScreenLayout, Long: {c.screenLayoutLong}");
            contents.AppendLine($"* ScreenLayout, Round: {c.screenLayoutRound}");
            contents.AppendLine($"* TouchScreen: {c.touchScreen}");
            contents.AppendLine($"* UiMode, Night: {c.uiModeNight}");
            contents.AppendLine($"* UiMode, Type: {c.uiModeType}");  
      
            contents.AppendLine($"* Locales ({c.locales.Length}):");
            for (int i = 0; i < c.locales.Length; i++)
            {
                var l = c.locales[i];
                contents.AppendLine($"* Locale[{i}] {l.country}-{l.language}");
            };  
      
            [Debug.Log](Debug.Log.html)($"Current Config:\n{contents}");
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

