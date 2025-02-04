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

#  [GUI](GUI.html).skin

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

public static [GUISkin](GUISkin.html) skin;

### Description

The global skin to use.

You can set this at any point to change the look of your GUI. If you set it to
null, the skin will revert to the default Unity skin.

    
    
    // Press space to change between added [GUI](GUI.html) skins.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GUISkin](GUISkin.html)[] s1;  
      
        private float hSliderValue = 0.0F;
        private float vSliderValue = 0.0F;
        private float hSValue = 0.0F;
        private float vSValue = 0.0F;
        private int cont = 0;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKeyDown](Input.GetKeyDown.html)([KeyCode.Space](KeyCode.Space.html)))
            {
                cont++;
            }
        }  
      
        void OnGUI()
        {
            [GUI.skin](GUI-skin.html) = s1[cont % s1.Length];  
      
            if (s1.Length == 0)
            {
                [Debug.LogError](Debug.LogError.html)("Assign at least 1 skin on the array");
                return;
            }  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 10, 100, 20), "Hello World!");
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(10, 50, 50, 50), "A BOX");  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 110, 70, 30), "A button"))
            {
                [Debug.Log](Debug.Log.html)("[Button](UIElements.Button.html) has been pressed");
            }  
      
            hSliderValue = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(10, 150, 100, 30), hSliderValue, 0.0F, 10.0F);
            vSliderValue = [GUI.VerticalSlider](GUI.VerticalSlider.html)(new [Rect](Rect.html)(10, 170, 100, 30), vSliderValue, 10.0F, 0.0F);
            hSValue = [GUI.HorizontalScrollbar](GUI.HorizontalScrollbar.html)(new [Rect](Rect.html)(10, 210, 100, 30), hSValue, 1.0F, 0.0F, 10.0F);
            vSValue = [GUI.VerticalScrollbar](GUI.VerticalScrollbar.html)(new [Rect](Rect.html)(10, 230, 100, 30), vSValue, 1.0F, 10.0F, 0.0F);
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

