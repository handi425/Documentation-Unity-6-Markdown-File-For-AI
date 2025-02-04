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

#  [Bounds](Bounds.html).extents

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

public [Vector3](Vector3.html) extents;

### Description

The extents of the Bounding Box. This is always half of the [size](Bounds-
size.html) of the Bounds.

**Note:** If [Bounds.extents](Bounds-extents.html) has a negative value for
any axis, [Bounds.Contains](Bounds.Contains.html) always returns False.

    
    
    //Attach this script to a visible [GameObject](GameObject.html).
    //Click on the [GameObject](GameObject.html) to expand it and output the Bound extents to the Console.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Collider](Collider.html) m_ObjectCollider;
        public [Vector3](Vector3.html) m_MyScale;  
      
        void Start()
        {
            //Fetch the [GameObject](GameObject.html)'s collider (make sure they have a [Collider](Collider.html) component)
            m_ObjectCollider = gameObject.GetComponent<[Collider](Collider.html)>();
            //Output the [GameObject](GameObject.html)'s [Collider](Collider.html) Bound extents
            [Debug.Log](Debug.Log.html)("extents : " + m_ObjectCollider.bounds.extents);
        }  
      
        //Detect when the user clicks the [GameObject](GameObject.html)
        void OnMouseDown()
        {
            //Change the scale of the [GameObject](GameObject.html) to the size you define in the Inspector
            transform.localScale = m_MyScale;
            //Output the extents of the [Bounds](Bounds.html) after clicking the [GameObject](GameObject.html). Extents change to half of the scale.
            [Debug.Log](Debug.Log.html)("extents : " + m_ObjectCollider.bounds.extents);
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

