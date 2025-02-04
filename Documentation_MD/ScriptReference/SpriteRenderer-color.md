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

#  [SpriteRenderer](SpriteRenderer.html).color

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

public [Color](Color.html) color;

### Description

Rendering color for the Sprite graphic.

The selected vertex color becomes the rendering color, and is accessible in a
pixel shader. The default color is white when no color is selected.

    
    
    //This example outputs Sliders that control the red green and blue elements of a sprite's color
    //Attach this to a [GameObject](GameObject.html) and attach a [SpriteRenderer](SpriteRenderer.html) component  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [SpriteRenderer](SpriteRenderer.html) m_SpriteRenderer;
        //The [Color](Color.html) to be assigned to the [Renderer](Renderer.html)’s [Material](Material.html)
        [Color](Color.html) m_NewColor;  
      
        //These are the values that the [Color](Color.html) Sliders return
        float m_Red, m_Blue, m_Green;  
      
        void Start()
        {
            //Fetch the [SpriteRenderer](SpriteRenderer.html) from the [GameObject](GameObject.html)
            m_SpriteRenderer = GetComponent<[SpriteRenderer](SpriteRenderer.html)>();
            //Set the [GameObject](GameObject.html)'s [Color](Color.html) quickly to a set [Color](Color.html) (blue)
            m_SpriteRenderer.color = [Color.blue](Color-blue.html);
        }  
      
        void OnGUI()
        {
            //Use the Sliders to manipulate the RGB component of [Color](Color.html)
            //Use the [Label](UIElements.Label.html) to identify the [Slider](UIElements.Slider.html)
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 30, 50, 30), "Red: ");
            //Use the [Slider](UIElements.Slider.html) to change amount of red in the [Color](Color.html)
            m_Red = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(35, 25, 200, 30), m_Red, 0, 1);  
      
            //The [Slider](UIElements.Slider.html) manipulates the amount of green in the [GameObject](GameObject.html)
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 70, 50, 30), "Green: ");
            m_Green = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(35, 60, 200, 30), m_Green, 0, 1);  
      
            //This [Slider](UIElements.Slider.html) decides the amount of blue in the [GameObject](GameObject.html)
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 105, 50, 30), "Blue: ");
            m_Blue = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(35, 95, 200, 30), m_Blue, 0, 1);  
      
            //Set the [Color](Color.html) to the values gained from the Sliders
            m_NewColor = new [Color](Color.html)(m_Red, m_Green, m_Blue);  
      
            //Set the [SpriteRenderer](SpriteRenderer.html) to the [Color](Color.html) defined by the Sliders
            m_SpriteRenderer.color = m_NewColor;
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

