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

#  [Bounds](Bounds.html).Intersects

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

public bool Intersects([Bounds](Bounds.html) bounds);

### Description

Does another bounding box intersect with this bounding box?

Check if the bounding box comes into contact with another bounding box. This
returns a Boolean that is set to true if there is an intersection between
bounds. Two bounds are intersecting if there is at least one point which is
contained by both bounds.

    
    
    //Attach this script to an empty [GameObject](GameObject.html). Create 2 more GameObjects and attach a [Collider](Collider.html) component on each. Choose these as the "My Object" and "New Object" in the Inspector.
    //This script allows you to move your main [GameObject](GameObject.html) left to right. If it intersects with the other, it outputs the message to the Console.  
      
    using UnityEngine;  
      
    public class BoundsIntersectExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) m_MyObject, m_NewObject;
        [Collider](Collider.html) m_Collider, m_Collider2;  
      
        void Start()
        {
            //Check that the first [GameObject](GameObject.html) exists in the Inspector and fetch the [Collider](Collider.html)
            if (m_MyObject != null)
                m_Collider = m_MyObject.GetComponent<[Collider](Collider.html)>();  
      
            //Check that the second [GameObject](GameObject.html) exists in the Inspector and fetch the [Collider](Collider.html)
            if (m_NewObject != null)
                m_Collider2 = m_NewObject.GetComponent<[Collider](Collider.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //If the first [GameObject](GameObject.html)'s [Bounds](Bounds.html) enters the second [GameObject](GameObject.html)'s [Bounds](Bounds.html), output the message
            if (m_Collider.bounds.Intersects(m_Collider2.bounds))
            {
                [Debug.Log](Debug.Log.html)("[Bounds](Bounds.html) intersecting");
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

