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

# ResourcesAPI

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Derive from this base class to provide alternative implementations to the C#
behavior of specific [Resources](Resources.html) methods.

The example provided logs the time taken to handle slower Resources APIs to
the player or editor log.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Diagnostics;
    using UnityEngine;
    using Object = UnityEngine.Object;
    using [Debug](Debug.html) = UnityEngine.Debug;  
      
    public class ResourcesPerformanceLogger : [ResourcesAPI](ResourcesAPI.html)
    {
        [RuntimeInitializeOnLoadMethod]
        static void OnRuntimeMethodLoad()
        {
            [ResourcesAPI.overrideAPI](ResourcesAPI-overrideAPI.html) = new ResourcesPerformanceLogger();
        }  
      
        protected override Object[] FindObjectsOfTypeAll(Type systemTypeInstance)
        {
            Stopwatch timer = new Stopwatch();
            timer.Start();
            Object[] results = base.FindObjectsOfTypeAll(systemTypeInstance);
            timer.Stop();
            [Debug.Log](Debug.Log.html)($"FindObjectsOfTypeAll({systemTypeInstance}) [Time](Time.html): {timer.Elapsed}");
            return results;
        }  
      
        protected override [Shader](Shader.html) FindShaderByName(string name)
        {
            Stopwatch timer = new Stopwatch();
            timer.Start();
            [Shader](Shader.html) result = base.FindShaderByName(name);
            timer.Stop();
            [Debug.Log](Debug.Log.html)($"FindShaderByName({name}) [Time](Time.html): {timer.Elapsed}");
            return result;
        }  
      
        protected override Object[] LoadAll(string path, Type systemTypeInstance)
        {
            Stopwatch timer = new Stopwatch();
            timer.Start();
            Object[] results = base.LoadAll(path, systemTypeInstance);
            timer.Stop();
            [Debug.Log](Debug.Log.html)($"LoadAll({path}, {systemTypeInstance}) [Time](Time.html): {timer.Elapsed}");
            return results;
        }
    }
    

### Static Properties

[overrideAPI](ResourcesAPI-overrideAPI.html)| The specific ResourcesAPI
instance to use to handle overridden Resources methods.  
---|---  
  
### Protected Methods

[FindObjectsOfTypeAll](ResourcesAPI.FindObjectsOfTypeAll.html)| Override for
customizing the behavior of the Resources.FindObjectsOfTypeAll function.  
---|---  
[FindShaderByName](ResourcesAPI.FindShaderByName.html)| Override for
customizing the behavior of the Shader.Find function.  
[Load](ResourcesAPI.Load.html)| Override for customizing the behavior of the
Resources.Load function.  
[LoadAll](ResourcesAPI.LoadAll.html)| Override for customizing the behavior of
the Resources.LoadAll function.  
[LoadAsync](ResourcesAPI.LoadAsync.html)| Override for customizing the
behavior of the Resources.LoadAsync function.  
[UnloadAsset](ResourcesAPI.UnloadAsset.html)| Override for customizing the
behavior of the Resources.Unload function.  
  
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

