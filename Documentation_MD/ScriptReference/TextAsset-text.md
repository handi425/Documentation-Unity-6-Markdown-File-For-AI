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

#  [TextAsset](TextAsset.html).text

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

[Switch to Manual](../Manual/class-TextAsset.html "Go to TextAsset Component
in the Manual")

public string text;

### Description

The text contents of the file as a string. (Read Only)

Encodings are detected and interpreted automatically. Supported encodings are:

  * UTF-32 Big or Little Endian with a byte order mark,
  * UTF-16 Big or Little Endian with a byte order mark,
  * UTF-8 with a byte order mark,
  * UTF-8 without a byte order mark. This encoding is used as a fallback, if the above encodings can't decode the file without missing characters.

To use a specific encoding to decode a file, use [TextAsset.bytes](TextAsset-
bytes.html) and C# encoding classes.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [TextAsset](TextAsset.html) asset;  
      
        void Start()
        {
            [Debug.Log](Debug.Log.html)(asset.text);
        }
    }
    

Additional resources: [bytes](TextAsset-bytes.html),
[GetData](TextAsset.GetData.html), [Text Assets](../Manual/class-
TextAsset.html).

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

