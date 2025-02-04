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

#  [Color](Color.html).HSVToRGB

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

public static [Color](Color.html) HSVToRGB(float H, float S, float V);

## Declaration

public static [Color](Color.html) HSVToRGB(float H, float S, float V, bool
hdr);

### Parameters

H | Hue [0..1].  
---|---  
S | Saturation [0..1].  
V | Brightness value [0..1].  
hdr | Output HDR colours. If true, the returned colour will not be clamped to [0..1].  
  
### Returns

**Color** An opaque colour with HSV matching the input.

### Description

Creates an RGB colour from HSV input.

Creates an RGB color from the hue, saturation and value of the input.

    
    
    //Create three Sliders ( **Create** >**UI** >**Slider**)
    //These are for manipulating the hue, saturation and value levels of the [Color](Color.html).  
      
    //Attach this script to a [GameObject](GameObject.html). Make sure it has a [Renderer](Renderer.html) component.
    //Click on the [GameObject](GameObject.html) and attach each of the Sliders and Texts to the fields in the Inspector.  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class ColorHSVtoRGBExample : [MonoBehaviour](MonoBehaviour.html)
    {
        float m_Hue;
        float m_Saturation;
        float m_Value;
        //These are the Sliders that control the values. Remember to attach them in the Inspector window.
        public [Slider](UIElements.Slider.html) m_SliderHue, m_SliderSaturation, m_SliderValue;  
      
        //Make sure your [GameObject](GameObject.html) has a [Renderer](Renderer.html) component in the Inspector window
        [Renderer](Renderer.html) m_Renderer;  
      
        void Start()
        {
            //Fetch the [Renderer](Renderer.html) component from the [GameObject](GameObject.html) with this script attached
            m_Renderer = GetComponent<[Renderer](Renderer.html)>();  
      
            //Set the maximum and minimum values for the Sliders
            m_SliderHue.maxValue = 1;
            m_SliderSaturation.maxValue = 1;
            m_SliderValue.maxValue = 1;  
      
            m_SliderHue.minValue = 0;
            m_SliderSaturation.minValue = 0;
            m_SliderValue.minValue = 0;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //These are the Sliders that determine the amount of the hue, saturation and value in the [Color](Color.html)
            m_Hue = m_SliderHue.value;
            m_Saturation = m_SliderSaturation.value;
            m_Value = m_SliderValue.value;  
      
            //Create an RGB color from the HSV values from the Sliders
            //Change the [Color](Color.html) of your [GameObject](GameObject.html) to the new [Color](Color.html)
            m_Renderer.material.color = [Color.HSVToRGB](Color.HSVToRGB.html)(m_Hue, m_Saturation, m_Value);
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

