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
[AsyncReadManager](Unity.IO.LowLevel.Unsafe.AsyncReadManager.html).OpenFileAsync

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
[Unity.IO.LowLevel.Unsafe.FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html)
OpenFileAsync(string fileName);

### Parameters

fileName | The path to the file to be opened.  
---|---  
  
### Returns

**FileHandle** The FileHandle of the file being opened. Use the FileHandle to
check the status of the open operation, to read the file, and to close the
file when done.

### Description

Opens the file asynchronously.

**Note:** WebGL builds do not support using `AsyncReadManager` to open files
from a remote web server; for example, from the path
`Application.streamingAssetsPath` which maps to a URL on a remote web server.

    
    
    using System.IO;
    using Unity.IO.LowLevel.Unsafe;
    using UnityEngine;  
      
    class AsyncOpenSample : [MonoBehaviour](MonoBehaviour.html)
    {
        [FileHandle](Unity.IO.LowLevel.Unsafe.FileHandle.html) fileHandle;
        public unsafe void Start()
        {
            string filePath = Path.Combine([Application.streamingAssetsPath](Application-streamingAssetsPath.html), "myfile.bin");  
      
            fileHandle = [AsyncReadManager.OpenFileAsync](Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html)(filePath);
        }  
      
        public unsafe void [Update](PlayerLoop.Update.html)()
        {
            if (fileHandle.IsValid() && fileHandle.JobHandle.IsCompleted)
            {
                fileHandle.Close().Complete();
            }
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

