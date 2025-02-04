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

#  [Bounds](Bounds.html).center

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

public [Vector3](Vector3.html) center;

### Description

The center of the bounding box.

    
    
    using UnityEngine;  
      
    public class ColliderBounds : [MonoBehaviour](MonoBehaviour.html)
    {
        [Collider](Collider.html) m_Collider;
        [Vector3](Vector3.html) m_Center;
        [Vector3](Vector3.html) m_Size, m_Min, m_Max;  
      
        void Start()
        {
            //Fetch the [Collider](Collider.html) from the [GameObject](GameObject.html)
            m_Collider = GetComponent<[Collider](Collider.html)>();
            //Fetch the center of the [Collider](Collider.html) volume
            m_Center = m_Collider.bounds.center;
            //Fetch the size of the [Collider](Collider.html) volume
            m_Size = m_Collider.bounds.size;
            //Fetch the minimum and maximum bounds of the [Collider](Collider.html) volume
            m_Min = m_Collider.bounds.min;
            m_Max = m_Collider.bounds.max;
            //Output this data into the console
            OutputData();
        }  
      
        void OutputData()
        {
            //Output to the console the center and size of the [Collider](Collider.html) volume
            [Debug.Log](Debug.Log.html)("[Collider](Collider.html) Center : " + m_Center);
            [Debug.Log](Debug.Log.html)("[Collider](Collider.html) Size : " + m_Size);
            [Debug.Log](Debug.Log.html)("[Collider](Collider.html) bound Minimum : " + m_Min);
            [Debug.Log](Debug.Log.html)("[Collider](Collider.html) bound Maximum : " + m_Max);
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

