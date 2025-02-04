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

# DownloadHandlerScript Constructor

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

public DownloadHandlerScript();

### Description

Create a DownloadHandlerScript which allocates new buffers when passing data
to callbacks.

This default constructor places this DownloadHanderScript into _non-
preallocated mode_. This affects the operation of the ReceiveData callback.  
  
When in non-preallocated mode, a new managed byte array will be allocated each
time ReceiveData is called, and the length of the array passed to ReceiveData
will always be equal to the number of new bytes available for consumption.  
  
This is convenient, but may cause undesirable garbage collection. If your use
case requires an implementation which avoids unnecessary garbage collection,
use preallocated mode instead.

* * *

## Declaration

public DownloadHandlerScript(byte[] preallocatedBuffer);

### Parameters

preallocatedBuffer | A byte buffer into which data will be copied, for use by [DownloadHandler.ReceiveData](Networking.DownloadHandler.ReceiveData.html).  
---|---  
  
### Description

Create a DownloadHandlerScript which reuses a preallocated buffer to pass data
to callbacks.

This constructor places this
[DownloadHandlerScript](Networking.DownloadHandlerScript.html) into
_preallocated mode_. This affects the operation of the
[DownloadHandler.ReceiveData](Networking.DownloadHandler.ReceiveData.html)
callback.  
  
When in preallocated mode, the `preallocatedBuffer` byte array will be
repeatedly reused to pass data to the
[DownloadHandler.ReceiveData](Networking.DownloadHandler.ReceiveData.html)
callback, instead of allocating new buffers each time. The system will not
zero-out the array between uses, so the `dataLength` argument to
[DownloadHandler.ReceiveData](Networking.DownloadHandler.ReceiveData.html)
must be used to discover which bytes are new.  
  
When in this mode, the
[DownloadHandlerScript](Networking.DownloadHandlerScript.html) will not
allocate any memory during the download or processing of HTTP response data.
If your use case is sensitive to garbage collection, usage of preallocated
mode is recommended.

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

