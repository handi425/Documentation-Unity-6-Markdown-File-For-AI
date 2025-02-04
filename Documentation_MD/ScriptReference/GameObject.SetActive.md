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

#  [GameObject](GameObject.html).SetActive

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

public void SetActive(bool value);

### Parameters

value | The active state to set, where `true` sets the GameObject to active and `false` sets it to inactive.  
---|---  
  
### Description

Activates or deactivates the GameObject locally, according to the value of the
supplied parameter.

`SetActive` only sets the local state of the GameObject, represented by the
value of [GameObject.activeSelf](GameObject-activeSelf.html). Changing the
value of [GameObject.activeSelf](GameObject-activeSelf.html) has no effect on
the value of [GameObject.activeInHierarchy](GameObject-activeInHierarchy.html)
if `activeInHierarchy` is `false` because of an inactive parent object.  
  
Deactivating a GameObject disables each component, including attached
renderers, colliders, rigidbodies, and scripts. For example, Unity will no
longer call [MonoBehaviour.Update](MonoBehaviour.Update.html) on a script
attached to a deactivated GameObject. Deactivating a GameObject also stops all
coroutines attached to it.  
  
**Note:** If the call to `SetActive` changes the value of
[GameObject.activeInHierarchy](GameObject-activeInHierarchy.html), this
triggers [MonoBehaviour.OnEnable](MonoBehaviour.OnEnable.html) or
[MonoBehaviour.OnDisable](MonoBehaviour.OnDisable.html) on all attached
MonoBehaviour scripts.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GameObject](GameObject.html)[] cubes = new [GameObject](GameObject.html)[10];
        public float timer, interval = 2f;  
      
        void Start()
        {
            [Vector3](Vector3.html) pos = new [Vector3](Vector3.html)(-5, 0, 0);  
      
            for (int i = 0; i < 10; i++)
            {
                cubes[i] = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                cubes[i].transform.position = pos;
                cubes[i].name = "Cube_" + i;
                pos.x++;
            }
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            timer += [Time.deltaTime](Time-deltaTime.html);
            if (timer >= interval)
            {
                for (int i = 0; i < 10; i++)
                {
                    int randomValue = [Random.Range](Random.Range.html)(0, 2);
                    if (randomValue == 0)
                    {
                        cubes[i].SetActive(false);
                    }
                    else  cubes[i].SetActive(true);
                }
                timer = 0;
            }
        }
    }
    

Additional resources: [GameObject.activeSelf](GameObject-activeSelf.html),
[GameObject.SetGameObjectsActive](GameObject.SetGameObjectsActive.html)

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

