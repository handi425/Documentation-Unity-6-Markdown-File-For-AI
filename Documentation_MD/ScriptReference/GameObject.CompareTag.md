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

#  [GameObject](GameObject.html).CompareTag

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

## Declaration

public bool CompareTag(string tag);

### Parameters

tag | The tag to check for on the GameObject.  
---|---  
  
### Returns

**bool** `true` if the GameObject has the given tag, `false` otherwise.

### Description

Checks if the specified tag is attached to the GameObject.

The example below calls `CompareTag` on a [Collider](Collider.html) to check
if it has the `Player` tag.

    
    
    // Immediate death trigger.
    // Destroys any colliders that enter the trigger, if they are tagged "Player".
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnTriggerEnter([Collider](Collider.html) other)
        {
            if (other.gameObject.CompareTag("Player"))
            {
                Destroy(other.gameObject);
            }
        }
    }
    

Additional resources: [GameObject.FindWithTag](GameObject.FindWithTag.html)

* * *

## Declaration

public bool CompareTag([TagHandle](TagHandle.html) tag);

### Parameters

tag | A [TagHandle](TagHandle.html) representing the tag to check for on the GameObject.  
---|---  
  
### Returns

**bool** `true` if the GameObject has the given tag, `false` otherwise.

### Description

Checks if the specified tag is attached to the GameObject.

This overload of the method, which takes a [TagHandle](TagHandle.html), can be
faster than the overload which takes a string, particularly if the same
`TagHandle` can be reused for many calls.  
  
The example below calls `CompareTag` with a `TagHandle` on a
[Collider](Collider.html) to check if it has the `Player` tag:

    
    
    // Immediate death trigger.
    // Destroys any colliders that enter the trigger, if they are tagged "Player".
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [TagHandle](TagHandle.html) _playerTag;
        public void OnEnable()
        {
            _playerTag = [TagHandle.GetExistingTag](TagHandle.GetExistingTag.html)("Player");
        }  
      
        void OnTriggerEnter([Collider](Collider.html) other)
        {
            if (other.gameObject.CompareTag(_playerTag))
            {
                Destroy(other.gameObject);
            }
        }
    }

Additional resources: [TagHandle](TagHandle.html)

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

