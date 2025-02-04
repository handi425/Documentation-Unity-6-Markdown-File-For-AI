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
[ContentLoadInterface](Unity.Loading.ContentLoadInterface.html).LoadContentFileAsync

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

public static [Unity.Loading.ContentFile](Unity.Loading.ContentFile.html)
LoadContentFileAsync([Unity.Content.ContentNamespace](Unity.Content.ContentNamespace.html)
nameSpace, string filename, NativeArray<ContentFile> dependencies,
[Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html) dependentFence);

### Parameters

nameSpace | The [ContentNamespace](Unity.Content.ContentNamespace.html) used to filter the results.  
---|---  
filename | Path of the file on disk.  
dependencies | List of the [ContentFile](Unity.Loading.ContentFile.html)s that will be referenced by the file being loaded. The ordering must match the ordering returned from the build process. [ContentFile.GlobalTableDependency](Unity.Loading.ContentFile.GlobalTableDependency.html) can be used to indicate that the PersistentManager should be used to resolve references. This allows references to files such as "unity default resources".  
dependentFence | The load will not begin until this [JobHandle](Unity.Jobs.JobHandle.html) completes. A default [JobHandle](Unity.Jobs.JobHandle.html) can be used if there is no dependency.  
  
### Returns

**ContentFile** Handle to access the results of the load process.

### Description

Loads a serialized file asynchronously from disk.

The status of the load operation can be accessed using the returned
[ContentFile](Unity.Loading.ContentFile.html). Objects loaded with this
function will not be garbage collected; the user is responsible for calling
[ContentFile.UnloadAsync](Unity.Loading.ContentFile.UnloadAsync.html) to free
resources when they are no longer required. The user must call
[ContentFile.UnloadAsync](Unity.Loading.ContentFile.UnloadAsync.html) even if
the load fails.

    
    
    using System.Collections;
    using Unity.Collections;
    using Unity.Content;
    using Unity.Loading;
    using UnityEngine;  
      
    public class SampleBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        public IEnumerator Start()
        {
            NativeArray<[ContentFile](Unity.Loading.ContentFile.html)> empty = new NativeArray<[ContentFile](Unity.Loading.ContentFile.html)>();
            [ContentFile](Unity.Loading.ContentFile.html) depFileHandle = [ContentLoadInterface.LoadContentFileAsync](Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html)([ContentNamespace.Default](Unity.Content.ContentNamespace.Default.html), "path/to/depfile", empty);  
      
            NativeArray<[ContentFile](Unity.Loading.ContentFile.html)> depFiles = new NativeArray<[ContentFile](Unity.Loading.ContentFile.html)>(1, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            depFiles[0] = depFileHandle;
            [ContentFile](Unity.Loading.ContentFile.html) rootFileHandle = [ContentLoadInterface.LoadContentFileAsync](Unity.Loading.ContentLoadInterface.LoadContentFileAsync.html)([ContentNamespace.Default](Unity.Content.ContentNamespace.Default.html), "path/to/rootfile", depFiles);
            depFiles.Dispose();  
      
            // yield coroutine until loading is complete
            while (rootFileHandle.LoadingStatus == [LoadingStatus.InProgress](Unity.Loading.LoadingStatus.InProgress.html))
                yield return null;  
      
            ulong localFileIdentifierOfObjectIWant = 25;
            [GameObject](GameObject.html) obj = ([GameObject](GameObject.html))rootFileHandle.GetObject(localFileIdentifierOfObjectIWant);  
      
            // When done using obj. unload both files.
            [ContentFileUnloadHandle](Unity.Loading.ContentFileUnloadHandle.html) unloadHandleRoot = rootFileHandle.UnloadAsync();
            [ContentFileUnloadHandle](Unity.Loading.ContentFileUnloadHandle.html) unloadHandleDep = depFileHandle.UnloadAsync();  
      
            // yield coroutine until loading is complete
            while (!unloadHandleRoot.IsCompleted || !unloadHandleRoot.IsCompleted)
                yield return null;  
      
            // file is now completly unloaded. obj has been deleted
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

