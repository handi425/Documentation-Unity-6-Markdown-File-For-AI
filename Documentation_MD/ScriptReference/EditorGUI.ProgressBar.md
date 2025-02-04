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

#  [EditorGUI](EditorGUI.html).ProgressBar

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

public static void ProgressBar([Rect](Rect.html) position, float value, string
text);

### Parameters

totalPosition | Rectangle on the screen to use in total for both the control.  
---|---  
value | Value that is shown.  
  
### Description

Makes a progress bar.

Value goes from 0 to 1, where 0 means 0% of the bar filled and 1 means the bar
is at 100% fully filled  
  
![](../StaticFiles/ScriptRefImages/EditorGUIProgressBar.png)  
_Progress bar in an Editor Window._

    
    
    using UnityEngine;
    using System.Collections;
    using [UnityEditor](UnityEditor.html);  
      
    // Draw the armor and damage with bars in an [Editor](Editor.html) Window  
      
    public class EditorGUIProgressBar : [EditorWindow](EditorWindow.html)
    {
        float armor = 20;
        float damage  = 80;  
      
        [[MenuItem](MenuItem.html)("Examples/[Display](Display.html) Info")]  
      
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUIProgressBar), false, "[DisplayInfo](DisplayInfo.html)");
            window.Show();
        }  
      
        void OnGUI()
        {
            armor = [EditorGUI.IntSlider](EditorGUI.IntSlider.html)(new [Rect](Rect.html)(3, 3, position.width - 6, 15), "Armor", [Mathf.RoundToInt](Mathf.RoundToInt.html)(armor), 0, 100);
            damage = [EditorGUI.IntSlider](EditorGUI.IntSlider.html)(new [Rect](Rect.html)(3, 25, position.width - 6, 15), "Damage", [Mathf.RoundToInt](Mathf.RoundToInt.html)(damage), 0, 100);  
      
            [EditorGUI.ProgressBar](EditorGUI.ProgressBar.html)(new [Rect](Rect.html)(3, 45, position.width - 6, 20), armor / 100, "Armor");
            [EditorGUI.ProgressBar](EditorGUI.ProgressBar.html)(new [Rect](Rect.html)(3, 70, position.width - 6, 20), damage / 100, "Damage");
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

