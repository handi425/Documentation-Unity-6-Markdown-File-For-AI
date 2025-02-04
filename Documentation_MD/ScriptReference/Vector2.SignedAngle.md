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

#  [Vector2](Vector2.html).SignedAngle

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

public static float SignedAngle([Vector2](Vector2.html) from,
[Vector2](Vector2.html) to);

### Parameters

from | The vector from which the angular difference is measured.  
---|---  
to | The vector to which the angular difference is measured.  
  
### Returns

**float** The signed angle in degrees between the two vectors.

### Description

Gets the signed angle in degrees between `from` and `to`.

The angle returned is the signed counterclockwise angle between the two
vectors.  
Note: The angle returned will always be between -180 and 180 degrees, because
the method returns the smallest angle between the vectors. That is, it will
never return a reflex angle. Angles are calculated from world origin point
(0,0,0) as the vertex.  
Additional resources: [Angle](Vector2.Angle.html) function.

    
    
    using UnityEngine;  
      
    public class Vector : [MonoBehaviour](MonoBehaviour.html)
    {
        //Use these to get the [GameObject](GameObject.html)'s positions
        [Vector2](Vector2.html) m_MyFirstVector;
        [Vector2](Vector2.html) m_MySecondVector;  
      
        float m_Angle;  
      
        //You must assign to these two GameObjects in the Inspector
        public [GameObject](GameObject.html) m_MyObject;
        public [GameObject](GameObject.html) m_MyOtherObject;  
      
        void Start()
        {
            //Initialise the Vector
            m_MyFirstVector = [Vector2.zero](Vector2-zero.html);
            m_MySecondVector = [Vector2.zero](Vector2-zero.html);
            m_Angle = 0.0f;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //Fetch the first [GameObject](GameObject.html)'s position
            m_MyFirstVector = new [Vector2](Vector2.html)(m_MyObject.transform.position.x, m_MyObject.transform.position.y);
            //Fetch the second [GameObject](GameObject.html)'s position
            m_MySecondVector = new [Vector2](Vector2.html)(m_MyOtherObject.transform.position.x, m_MyOtherObject.transform.position.y);
            //Find the angle for the two Vectors
            m_Angle = [Vector2.SignedAngle](Vector2.SignedAngle.html)(m_MyFirstVector, m_MySecondVector);  
      
            //Draw lines from origin point to Vectors
            [Debug.DrawLine](Debug.DrawLine.html)([Vector2.zero](Vector2-zero.html), m_MyFirstVector, [Color.magenta](Color-magenta.html));
            [Debug.DrawLine](Debug.DrawLine.html)([Vector2.zero](Vector2-zero.html), m_MySecondVector, [Color.blue](Color-blue.html));  
      
            //Log values of Vectors and angle in Console
            [Debug.Log](Debug.Log.html)("MyFirstVector: " + m_MyFirstVector);
            [Debug.Log](Debug.Log.html)("MySecondVector: " + m_MySecondVector);
            [Debug.Log](Debug.Log.html)("[Angle](UIElements.Angle.html) Between Objects: " + m_Angle);
        }  
      
        void OnGUI()
        {
            //Output the angle found above
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 25, 200, 40), "[Angle](UIElements.Angle.html) Between Objects" + m_Angle);
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

