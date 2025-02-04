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

#  [RectTransform](RectTransform.html).anchoredPosition

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

public [Vector2](Vector2.html) anchoredPosition;

### Description

The position of the pivot of this RectTransform relative to the anchor
reference point.

The Anchored Position is the position of the pivot of the RectTransform taking
into consideration the anchor reference point. The anchor reference point is
the position of the anchors. If the anchors are not together, Unity estimates
the four anchor positions using the pivot placement as a reference.  
  
**Note** : The Inspector changes which properties are exposed based on which
anchor preset is in use. For more information see [Rect
Transform](../Manual/class-RectTransform.html) and [Basic
Layout](../Manual/UIBasicLayout.html).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [RectTransform](RectTransform.html) m_RectTransform;
        float m_XAxis, m_YAxis;  
      
        void Start()
        {
            //Fetch the [RectTransform](RectTransform.html) from the [GameObject](GameObject.html)
            m_RectTransform = GetComponent<[RectTransform](RectTransform.html)>();
            //Initiate the x and y positions
            m_XAxis = 0.5f;
            m_YAxis = 0.5f;
        }  
      
        void OnGUI()
        {
            //The Labels show what the Sliders represent
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(0, 20, 150, 80), "Anchor [Position](UIElements.Position.html) X : ");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(300, 20, 150, 80), "Anchor [Position](UIElements.Position.html) Y : ");  
      
            //Create a horizontal [Slider](UIElements.Slider.html) that controls the x and y Positions of the anchors
            m_XAxis = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(150, 20, 100, 80), m_XAxis, -50.0f, 50.0f);
            m_YAxis = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(450, 20, 100, 80), m_YAxis, -50.0f, 50.0f);  
      
            //Detect a change in the [GUI](GUI.html) [Slider](UIElements.Slider.html)
            if ([GUI.changed](GUI-changed.html))
            {
                //Change the [RectTransform](RectTransform.html)'s anchored positions depending on the [Slider](UIElements.Slider.html) values
                m_RectTransform.anchoredPosition = new [Vector2](Vector2.html)(m_XAxis, m_YAxis);
            }
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

