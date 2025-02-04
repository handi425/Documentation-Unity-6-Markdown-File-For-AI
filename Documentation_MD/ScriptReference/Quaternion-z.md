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

#  [Quaternion](Quaternion.html).z

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

[Switch to Manual](../Manual/class-Quaternion.html "Go to Quaternion Component
in the Manual")

public float z;

### Description

Z component of the Quaternion. Don't modify this directly unless you know
quaternions inside out.

    
    
    //Create three Sliders (**Create** >**UI** >**Slider**) and three Text GameObjects (**Create** >**UI** >**Text**). These are for manipulating the x, y, and z values of the [Quaternion](Quaternion.html). The text will act as a label for each [Slider](UIElements.Slider.html), so position them appropriately.
    //Attach this script to a [GameObject](GameObject.html).
    //Click on the [GameObject](GameObject.html) and attach each of the Sliders and Texts to the fields in the Inspector.  
      
    //This script shows how the numbers placed into the x, y, and z components of a [Quaternion](Quaternion.html) effect the [GameObject](GameObject.html) when the w component is left at 1.
    //Use the Sliders to see the effects.  
      
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //These are the floats for the x, y, and z components of the quaternion
        float m_MyX, m_MyY, m_MyZ;
        //These are the Sliders that set the rotation. Remember to assign these in the Inspector
        public [Slider](UIElements.Slider.html) m_SliderX, m_SliderY, m_SliderZ;
        //These are the Texts that output the current value of the rotations. Remember to assign these in the Inspector
        public Text m_TextX, m_TextY, m_TextZ;  
      
        // Use this for initialization
        void Start()
        {
            //Initialise the x, y, and z components of the future [Quaternion](Quaternion.html)
            m_MyX = 0;
            m_MyY = 0;
            m_MyZ = 0;  
      
            //Set all the sliders max values to 1 so the [Quaternion](Quaternion.html) values don't go over 1
            m_SliderX.maxValue = 1;
            m_SliderY.maxValue = 1;
            m_SliderZ.maxValue = 1;  
      
            //Set all the sliders min values to -1 so the [Quaternion](Quaternion.html) values don't go under 1
            m_SliderX.minValue = -1;
            m_SliderY.minValue = -1;
            m_SliderZ.minValue = -1;
        }  
      
        //Change the [Quaternion](Quaternion.html) values depending on the values of the Sliders
        private static [Quaternion](Quaternion.html) Change(float x, float y, float z)
        {
            //Return the new [Quaternion](Quaternion.html)
            return new [Quaternion](Quaternion.html)(x, y , z, 1);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //[Update](PlayerLoop.Update.html) the x, y and z values to that of the sliders
            m_MyX = m_SliderX.value;
            m_MyY = m_SliderY.value;
            m_MyZ = m_SliderZ.value;
            //Output the current values of x, y, and z
            m_TextX.text = " X : " + m_MyX;
            m_TextY.text = " Y : " + m_MyY;
            m_TextZ.text = " Z : " + m_MyZ;  
      
            //[Rotate](UIElements.Rotate.html) the [GameObject](GameObject.html) by the new [Quaternion](Quaternion.html)
            transform.rotation = Change(m_MyX, m_MyY, m_MyZ);
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

