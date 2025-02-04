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

#  [BoxCollider](BoxCollider.html).size

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

[Switch to Manual](../Manual/class-BoxCollider.html "Go to BoxCollider
Component in the Manual")

public [Vector3](Vector3.html) size;

### Description

The size of the box, measured in the object's local space.

Use this to return or set the size of the BoxCollider component of a
GameObject. Unity measures the size in the GameObject's local space. Changing
the BoxCollider size scales it by the Transform’s scale.

    
    
    //Attach this script to a [GameObject](GameObject.html). Make sure the [GameObject](GameObject.html) has a [BoxCollider](BoxCollider.html) component (Unity Cubes have these automatically as long as they weren’t removed).
    //Create three Sliders ( **Create** >**UI** >**Slider**). These are for manipulating the x, y, and z values of the size.
    //Click on the [GameObject](GameObject.html) and attach each of the Sliders to the fields in the Inspector.
    //In Play [Mode](Scripting.GarbageCollector.Mode.html), click the [GameObject](GameObject.html) and enable [Gizmos](Gizmos.html) to visualize the [BoxCollider](BoxCollider.html).  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Make sure there is a [BoxCollider](BoxCollider.html) component attached to your [GameObject](GameObject.html)
        [BoxCollider](BoxCollider.html) m_Collider;
        float m_ScaleX, m_ScaleY, m_ScaleZ;
        public [Slider](UIElements.Slider.html) m_SliderX, m_SliderY, m_SliderZ;  
      
    
        void Start()
        {
            //Fetch the [Collider](Collider.html) from the [GameObject](GameObject.html)
            m_Collider = GetComponent<[BoxCollider](BoxCollider.html)>();
            //These are the starting sizes for the [Collider](Collider.html) component
            m_ScaleX = 1.0f;
            m_ScaleY = 1.0f;
            m_ScaleZ = 1.0f;  
      
            //Set all the sliders max values to 20 so the size values don't go above 20
            m_SliderX.maxValue = 20;
            m_SliderY.maxValue = 20;
            m_SliderZ.maxValue = 20;  
      
            //Set all the sliders min values to 1 so the size don't go below 1
            m_SliderX.minValue = 1;
            m_SliderY.minValue = 1;
            m_SliderZ.minValue = 1;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            m_ScaleX = m_SliderX.value;
            m_ScaleY = m_SliderY.value;
            m_ScaleZ = m_SliderZ.value;  
      
            m_Collider.size = new [Vector3](Vector3.html)(m_ScaleX, m_ScaleY, m_ScaleZ);
            [Debug.Log](Debug.Log.html)("Current [BoxCollider](BoxCollider.html) Size : " + m_Collider.size);
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

