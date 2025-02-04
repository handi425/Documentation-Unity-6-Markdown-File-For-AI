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

#  [Application](Application.html).lowMemory

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

### Description

The `Application._lowMemory` event occurs when your application receives a
low-memory notification from the device it is running on.

This only occurs when your application is running in the foreground. You can
release non-critical assets from memory (such as, textures and audio clips) to
avoid the application from being terminated. You can also load smaller
versions of such assets. In addtion, you should serialize any transient data
to permanent storage to avoid data loss if the app is terminated.  
  
The `Application._lowMemory` event is supported on iOS, Android, and Universal
Windows Platform (UWP) and it corresponds to the following callbacks on
different platforms:

  * **iOS** : `UIApplicationDelegate applicationDidReceiveMemoryWarning`
  * **Android** : `onLowMemory(`) and `onTrimMemory(level == TRIM_MEMORY_RUNNING_CRITICAL)`
  * **UWP** : `MemoryManager.AppMemoryUsageIncreased (AppMemoryUsageLevel == OverLimit)`

**Note:** For UWP, this event does not occur on desktop and only works on
memory constrained devices, such as HoloLens. The `OverLimit` threshold
specified by the OS in this case is so high that it's not reasonably possible
to reach it and trigger the event.  
  
Following example shows an example of handling the callback:

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;  
      
    class LowMemoryTrigger : [MonoBehaviour](MonoBehaviour.html)
    {
        List<[Texture2D](Texture2D.html)> _textures;  
      
        private void Start()
        {
            _textures = new List<[Texture2D](Texture2D.html)>();
            [Application.lowMemory](Application-lowMemory.html) += OnLowMemory;
        }  
      
        private void [Update](PlayerLoop.Update.html)()
        {
            // allocate textures until we run out of memory
            _textures.Add(new [Texture2D](Texture2D.html)(256, 256));
        }  
      
        private void OnLowMemory()
        {
            // release all cached textures
            _textures = new List<[Texture2D](Texture2D.html)>();
            [Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html)();
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

