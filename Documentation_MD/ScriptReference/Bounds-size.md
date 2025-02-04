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

#  [Bounds](Bounds.html).size

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

public [Vector3](Vector3.html) size;

### Description

The total size of the box. This is always twice as large as the
[extents](Bounds-extents.html).

_size.x_ is the width, _size.y_ is the height and _size.z_ is the depth of the
box. Note that _size_ is given in world size. A Bound surrounding a tall human
might have _size.y_ approximately 2.0f, meaning a 2 meter height body.

    
    
    //This script outputs the size of the [Collider](Collider.html) bounds to the console  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Collider](Collider.html) m_Collider;
        [Vector3](Vector3.html) m_Size;  
      
        void Start()
        {
            //Fetch the [Collider](Collider.html) from the [GameObject](GameObject.html)
            m_Collider = GetComponent<[Collider](Collider.html)>();  
      
            //Fetch the size of the [Collider](Collider.html) volume
            m_Size = m_Collider.bounds.size;  
      
            //Output to the console the size of the [Collider](Collider.html) volume
            [Debug.Log](Debug.Log.html)("[Collider](Collider.html) Size : " + m_Size);
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

