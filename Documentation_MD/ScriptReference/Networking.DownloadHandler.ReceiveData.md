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

#  [DownloadHandler](Networking.DownloadHandler.html).ReceiveData

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

protected bool ReceiveData(byte[] data, int dataLength);

### Parameters

data | A buffer containing unprocessed data, received from the remote server.  
---|---  
dataLength | The number of bytes in `data` which are new.  
  
### Returns

**bool** True if the download should continue, false to abort.

### Description

Callback, invoked as data is received from the remote server.

This callback is invoked on the main thread.  
  
Data arriving from the remote server for a
[DownloadHandlerScript](Networking.DownloadHandlerScript.html) is kept in a
temporary ringbuffer.  
  
When there is unprocessed data in the buffer, this method will be called once
per frame to hand chunks of that data to script. (If multiple datagrams arrive
within one frame, they will be combined before being passed to this callback.)
The data byte array contains the received data.  
  
When operating in non-preallocated mode, the system will allocate a new byte
array each time this callback is invoked. In this case, `data.Length` will be
equal to `dataLength`, and you may safely ignore the `dataLength` argument.  
  
When operating in preallocated mode, the data argument will be the byte array
passed in at construction time, and the dataLength argument indicates which
bytes in the byte array are new. (**Important:** The system does _not_ zero-
out the array between calls.)  
  
See DownloadHandlerScript.ctor for more information on allocation modes.

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

