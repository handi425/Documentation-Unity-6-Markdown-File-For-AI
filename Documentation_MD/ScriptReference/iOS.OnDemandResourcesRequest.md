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

# OnDemandResourcesRequest

class in UnityEngine.iOS

/

Inherits from:[AsyncOperation](AsyncOperation.html)

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

Represents a request for On Demand Resources (ODR). It's an
[AsyncOperation](AsyncOperation.html) and can be yielded in a coroutine.

**NOTE:** only available on iOS.  
  
Creating an [OnDemandResourcesRequest](iOS.OnDemandResourcesRequest.html) is
equivalent to calling [
NSBundleResourceRequest.beginAccessingResourcesWithCompletionHandler
](https://developer.apple.com/reference/foundation/nsbundleresourcerequest/1614840-beginaccessingresources).
The request will keep the on demand resource alive until either
[Dispose](iOS.OnDemandResourcesRequest.Dispose.html)() is called or the
request object is collected by a garbage collector, which is the equivalent of
calling [NSBundleResourceRequest.endAccessingResources
](https://developer.apple.com/reference/foundation/nsbundleresourcerequest/1614843-endaccessingresources).

    
    
    using UnityEngine;
    using UnityEngine.iOS;
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections;  
      
    public static class Loader
    {
        public static IEnumerator LoadAsset(string resourceName)
        {
            // Create the request
            var request = [OnDemandResources.PreloadAsync](iOS.OnDemandResources.PreloadAsync.html)(new string[] { "[Asset](VersionControl.Asset.html)'s ODR tag" });  
      
            // Wait until request is completed
            yield return request;  
      
            // Check for errors
            if (request.error != null)
                throw new Exception("ODR request failed: " + request.error);  
      
            // Get path to the resource and use it
            var path = request.GetResourcePath(resourceName);
            [Debug.Log](Debug.Log.html)(path);  
      
            // Call Dispose() when resource is no longer needed.
            request.Dispose();
        }
    }
    

### Properties

[error](iOS.OnDemandResourcesRequest-error.html)| Returns an error after
operation is complete.  
---|---  
[loadingPriority](iOS.OnDemandResourcesRequest-loadingPriority.html)| Sets the
priority for request.  
  
### Public Methods

[Dispose](iOS.OnDemandResourcesRequest.Dispose.html)| Release all resources
kept alive by On Demand Resources (ODR) request.  
---|---  
[GetResourcePath](iOS.OnDemandResourcesRequest.GetResourcePath.html)| Gets
file system's path to the resource available in On Demand Resources (ODR)
request.  
  
### Inherited Members

### Properties

[allowSceneActivation](AsyncOperation-allowSceneActivation.html)| Allow Scenes
to be activated as soon as it is ready.  
---|---  
[isDone](AsyncOperation-isDone.html)| Has the operation finished? (Read Only)  
[priority](AsyncOperation-priority.html)| Priority lets you tweak in which
order async operation calls will be performed.  
[progress](AsyncOperation-progress.html)| What's the operation's progress.
(Read Only)  
  
### Events

[completed](AsyncOperation-completed.html)| Event that is invoked upon
operation completion. An event handler that is registered in the same frame as
the call that creates it will be invoked next frame, even if the operation is
able to complete synchronously. If a handler is registered after the operation
has completed and has already invoked the complete event, the handler will be
called synchronously.  
---|---  
  
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

