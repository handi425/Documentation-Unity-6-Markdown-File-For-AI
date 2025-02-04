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

#  [PlayerSettings.iOS](PlayerSettings.iOS.html).hideHomeButton

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

public static bool hideHomeButton;

### Description

Specifies whether the home button should be hidden in the iOS build of this
application.

On iPhone X the home button is implemented as a system gesture (swipe up from
the bottom edge of the screen). The location of this virtual button is
indicated by a white bar. If this setting is enabled, the home button is
hidden from view whenever the user has not touched the screen for several
seconds. Note that iOS Human interface guidelines do not recommend enabling
this behavior for applications not containing passive viewing experiences such
as viewing a video or a photo slideshow. Home button can be hidden on runtime
by changing `iOS.Device.hideHomeButton` property.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class HideHomeButtonExample
    {
        // This example will create a [Menu](Menu.html) [Item](Progress.Item.html) called "Hide Home [Button](UIElements.Button.html)" under "Examples" submenu which when pressed will print the current value of hideHomeButton to console and then change it to "true"
        [[MenuItem](MenuItem.html)("Examples/Hide Home [Button](UIElements.Button.html)")]
        public static void SimpleExample()
        {
            // This will print the value of "Hide Home [Button](UIElements.Button.html)" property for [iOS](PlayerSettings.iOS.html) (in "Project [Settings](CameraEditor.Settings.html)/Player/Other [Settings](CameraEditor.Settings.html)") to the console 
            [Debug.Log](Debug.Log.html)("Hide Home [Button](UIElements.Button.html) : " + [PlayerSettings.iOS.hideHomeButton](PlayerSettings.iOS-hideHomeButton.html));
            
            // This will enable the "Hide Home [Button](UIElements.Button.html)" property for [iOS](PlayerSettings.iOS.html) (in "Project [Settings](CameraEditor.Settings.html)/Player/Other [Settings](CameraEditor.Settings.html)")
            [PlayerSettings.iOS.hideHomeButton](PlayerSettings.iOS-hideHomeButton.html) = true;
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

