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

#  [PlayerSettings.SplashScreen](PlayerSettings.SplashScreen.html).logos

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

public static SplashScreenLogo[] logos;

### Description

The collection of logos that is shown during the splash screen. Logos are
drawn in ascending order, starting from index 0, followed by 1, etc etc.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript
    {
        [[MenuItem](MenuItem.html)("[SplashScreen](PlayerSettings.SplashScreen.html)/AssignLogos")]
        public static void AssignLogos()
        {
            var logos = new [PlayerSettings.SplashScreenLogo](PlayerSettings.SplashScreenLogo.html)[2];  
      
            // Company logo
            [Sprite](Sprite.html) companyLogo = ([Sprite](Sprite.html))[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)("Assets/[SplashScreen](PlayerSettings.SplashScreen.html)/company logo.jpg", typeof([Sprite](Sprite.html)));
            logos[0] = [PlayerSettings.SplashScreenLogo.Create](PlayerSettings.SplashScreenLogo.Create.html)(2.5f, companyLogo);  
      
            // Set the Unity logo to be drawn after the company logo.
            logos[1] = [PlayerSettings.SplashScreenLogo.CreateWithUnityLogo](PlayerSettings.SplashScreenLogo.CreateWithUnityLogo.html)();  
      
            [PlayerSettings.SplashScreen.logos](PlayerSettings.SplashScreen-logos.html) = logos;
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

