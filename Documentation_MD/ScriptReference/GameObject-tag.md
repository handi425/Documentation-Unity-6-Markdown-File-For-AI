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

#  [GameObject](GameObject.html).tag

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

public string tag;

### Description

The tag assigned to the GameObject.

A tag can be used to identify a GameObject. Tags must be declared in the [Tags
and Layers manager](../Manual/class-TagManager.html) before using them.  
  
**Note:** Do not set a tag from [Awake()](MonoBehaviour.Awake.html) or
[OnValidate()](MonoBehaviour.OnValidate.html). The order in which `Awake` is
called is not deterministic between components and a tag can be overwritten
when its `Awake` is called. If you do this, Unity generates the warning
`SendMessage cannot be called during Awake, CheckConsistency, or OnValidate`.  
  
The example below sets the current GameObject's tag to "Player" and then
implements [MonoBehaviour.OnTriggerEnter](MonoBehaviour.OnTriggerEnter.html)
to check if the [Collider](Collider.html) on the other object involved in a
collision with this object is tagged "Enemy".

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            //Set the tag of this [GameObject](GameObject.html) to Player
            gameObject.tag = "Player";
        }  
      
        private void OnTriggerEnter([Collider](Collider.html) other)
        {
            //Check if the collider of the other [GameObject](GameObject.html) involved in the collision is tagged "Enemy"
            if (other.tag == "Enemy")
            {
                [Debug.Log](Debug.Log.html)("Triggered by Enemy");
            }
        }
    }
    

Additional resources: [GameObject.CompareTag](GameObject.CompareTag.html),
[MonoBehaviour](MonoBehaviour.html)

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

