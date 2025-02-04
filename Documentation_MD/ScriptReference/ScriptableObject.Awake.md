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

#  [ScriptableObject](ScriptableObject.html).Awake()

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

[Switch to Manual](../Manual/class-ScriptableObject.html "Go to
ScriptableObject Component in the Manual")

### Description

Called when an instance of `ScriptableObject` is created.

`Awake` is called when a new instance of a `ScriptableObject` is created.
Scenarios in which this happens include:

  * A new `ScriptableObject` is created as an asset via the [Create Asset menu](CreateAssetMenuAttribute.html) in the Editor
  * A new `ScriptableObject` is created programmatically using [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)
  * A `ScriptableObject` is loaded from an [AssetBundle](AssetBundle.html) at runtime
  * A scene which contains a reference to the `ScriptableObject` asset is loaded in the [Hierarchy window](../Manual/Hierarchy.html) for the first time, or on subsequent loads if the original instance has since been cleaned up by [Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html)
  * The `ScriptableObject` asset is selected in the [Project window](../Manual/ProjectView.html) for the first time, or on subsequent selections if the original instance has since been cleaned up by [Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html)

**Note** : ScriptableObjects created as assets in Edit mode are not recreated
on entering Play mode. To perform initialization work in a `ScriptableObject`
on entering Play mode, use
[ScriptableObject.OnEnable](ScriptableObject.OnEnable.html) instead.  
  
An example is given below. This example has two scripts. The first shown is
the [ScriptableObject](ScriptableObject.html) script. This implements code
which is separate from [MonoBehaviour](MonoBehaviour.html). The second is a
small [MonoBehaviour](MonoBehaviour.html) related script which accesses values
from the ScriptableObject script.

    
    
    // A [ScriptableObject](ScriptableObject.html) example script.
    // The A and B members implement features which
    // are unrelated to [MonoBehaviour](MonoBehaviour.html).  
      
    using UnityEngine;  
      
    public class ScriptObj : [ScriptableObject](ScriptableObject.html)
    {
        int a = 10;
        int[] b = new int[5] {0, 17, 34, 42, 67};  
      
        public int A
        {
            get {return a; }
        }  
      
        // return value in b array, or -1 if x is out-of-range
        public int B(int x)
        {
            if (x >= 0 && x < 5)
                return b[x];
            else
                return -1;
        }  
      
        public void Awake()
        {
            [Debug.Log](Debug.Log.html)("Awake");
        }  
      
        public void OnDestroy()
        {
            [Debug.Log](Debug.Log.html)("OnDestroy");
        }
    }
    

The following script makes use of the above ScriptableObject script.

    
    
    // create and access the ScriptObj  
      
    using UnityEngine;  
      
    public class ScriptObjExample : [MonoBehaviour](MonoBehaviour.html)
    {
        ScriptObj test;  
      
        void Start()
        {
            test = (ScriptObj)[ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)(typeof(ScriptObj));  
      
            print(test.A);
            print(test.B(3));
            print(test.B(-3));
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

