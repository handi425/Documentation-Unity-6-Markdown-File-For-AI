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

#  [Bounds](Bounds.html).Contains

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

public bool Contains([Vector3](Vector3.html) point);

### Description

Is `point` contained in the bounding box?

If the `point` passed into [Contains](Bounds.Contains.html) is inside the
bounding box a value of True is returned. Points on the min and max limits
(corners and edges) of the bounding box are considered inside.  
  
**Note:** If [Bounds.extents](Bounds-extents.html) contains a negative value
in any coordinate then [Bounds.Contains](Bounds.Contains.html) will always
return False.

    
    
    //Attach this script to a [GameObject](GameObject.html) with a [Collider](Collider.html) component
    //Create an empty [GameObject](GameObject.html) (**Create** >**Create Empty**) and attach it in the New [Transform](Transform.html) field in the Inspector of the first [GameObject](GameObject.html)
    //This script tells if a point  you specify (the position of the empty [GameObject](GameObject.html)) is within the first [GameObject](GameObject.html)’s [Collider](Collider.html)  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        //Make sure to assign this in the Inspector window
        public [Transform](Transform.html) m_NewTransform;
        [Collider](Collider.html) m_Collider;
        [Vector3](Vector3.html) m_Point;  
      
        void Start()
        {
            //Fetch the [Collider](Collider.html) from the [GameObject](GameObject.html) this script is attached to
            m_Collider = GetComponent<[Collider](Collider.html)>();
            //Assign the point to be that of the [Transform](Transform.html) you assign in the Inspector window
            m_Point = m_NewTransform.position;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //If the first [GameObject](GameObject.html)'s [Bounds](Bounds.html) contains the [Transform](Transform.html)'s position, output a message in the console
            if (m_Collider.bounds.Contains(m_Point))
            {
                [Debug.Log](Debug.Log.html)("[Bounds](Bounds.html) contain the point : " + m_Point);
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

