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

#
[ContentLoadInterface](Unity.Loading.ContentLoadInterface.html).LoadSceneAsync

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

public static
[Unity.Loading.ContentSceneFile](Unity.Loading.ContentSceneFile.html)
LoadSceneAsync([Unity.Content.ContentNamespace](Unity.Content.ContentNamespace.html)
nameSpace, string filename, string sceneName,
[Unity.Loading.ContentSceneParameters](Unity.Loading.ContentSceneParameters.html)
sceneParams, NativeArray<ContentFile> dependencies,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependentFence);

### Parameters

dependencies | List of the ContentFiles that will be referenced by the file being loaded. The ordering must match the ordering returned from the build process. [ContentFile.GlobalTableDependency](Unity.Loading.ContentFile.GlobalTableDependency.html) can be used to indicate that the PersistentManager should be used to resolve references. This allows references to files such as "unity default resources".  
---|---  
nameSpace | The ContentNamespace used to filter the results.  
filename | Path of the file on disk.  
sceneName | The name that will be applied to the scene.  
sceneParams | Struct that collects the various parameters into a single place.  
dependentFence | The load will not begin until this JobHandle completes.  
  
### Returns

**ContentSceneFile** Handle to access the results of the load process.

### Description

Loads a scene serialized file asynchronously from disk.

    
    
    using System.Collections;
    using Unity.Collections;
    using Unity.Content;
    using Unity.Loading;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class SampleBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        public IEnumerator Start()
        {
            NativeArray<[ContentFile](Unity.Loading.ContentFile.html)> empty = new NativeArray<[ContentFile](Unity.Loading.ContentFile.html)>();
            [ContentFile](Unity.Loading.ContentFile.html) depFileHandle = [ContentLoadInterface.LoadContentFileAsync](Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html)([ContentNamespace.Default](Unity.Content.ContentNamespace.Default.html), "path/to/depfile", empty);  
      
            var sceneParams = new [ContentSceneParameters](Unity.Loading.ContentSceneParameters.html)();
            sceneParams.loadSceneMode = [LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html);
            sceneParams.localPhysicsMode = [LocalPhysicsMode.None](SceneManagement.LocalPhysicsMode.None.html);
            sceneParams.autoIntegrate = false;  
      
            NativeArray<[ContentFile](Unity.Loading.ContentFile.html)> files = new NativeArray<[ContentFile](Unity.Loading.ContentFile.html)>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html), [NativeArrayOptions.ClearMemory](Unity.Collections.NativeArrayOptions.ClearMemory.html));
            files[0] = depFileHandle;
            [ContentSceneFile](Unity.Loading.ContentSceneFile.html) op = [ContentLoadInterface.LoadSceneAsync](Unity.Loading.ContentLoadInterface.LoadSceneAsync.html)([ContentNamespace.Default](Unity.Content.ContentNamespace.Default.html), "path/to/scene", "TestScene", sceneParams, files);
            files.Dispose();  
      
            // wait until the async loading process completes
            while (op.Status == [SceneLoadingStatus.InProgress](Unity.Loading.SceneLoadingStatus.InProgress.html))
                yield return null;  
      
            op.IntegrateAtEndOfFrame();  
      
            // wait one frame
            yield return null;  
      
            // scene is now loaded and integrated ...  
      
            // unload scene
            op.UnloadAtEndOfFrame();
            yield return null;  
      
            [ContentFileUnloadHandle](Unity.Loading.ContentFileUnloadHandle.html) unloadHandleDep = depFileHandle.UnloadAsync();  
      
            while (!unloadHandleDep.IsCompleted)
                yield return null;
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

