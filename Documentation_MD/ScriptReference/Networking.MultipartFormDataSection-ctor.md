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

# MultipartFormDataSection Constructor

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

public MultipartFormDataSection(byte[] data);

### Parameters

data | Data payload of this section.  
---|---  
  
### Description

Raw data section, unnamed and no `Content-Type` header.

Will not include either a filename or a `Content-Type` section header.

* * *

## Declaration

public MultipartFormDataSection(string name, byte[] data);

### Parameters

name | Section name.  
---|---  
data | Data payload of this section.  
  
### Description

Raw data section with a section name, no `Content-Type` header.

Identical to the prior constructor, but with a section name included.

* * *

## Declaration

public MultipartFormDataSection(string name, byte[] data, string contentType);

### Parameters

name | Section name.  
---|---  
data | Data payload of this section.  
contentType | The value for this section's `Content-Type` header.  
  
### Description

A raw data section with a section name and a `Content-Type` header.

* * *

## Declaration

public MultipartFormDataSection(string name, string data, Encoding encoding,
string contentType);

### Parameters

name | Section name.  
---|---  
data | String data payload for this section.  
contentType | The value for this section's `Content-Type` header.  
encoding | An encoding to marshal `data` to or from raw bytes.  
  
### Description

A named raw data section whose payload is derived from a string, with a
`Content-Type` header.

`data` will be encoded into raw bytes using `encoding`.

* * *

## Declaration

public MultipartFormDataSection(string name, string data, string contentType);

### Parameters

name | Section name.  
---|---  
data | String data payload for this section.  
contentType | The value for this section's `Content-Type` header.  
  
### Description

A named raw data section whose payload is derived from a UTF8 string, with a
`Content-Type` header.

For UTF-8 strings with custom `Content-Type` headers, use this constructor.
The data is returned in UTF-8 encoding and converted to raw bytes
appropriately.

* * *

## Declaration

public MultipartFormDataSection(string name, string data);

### Parameters

name | Section name.  
---|---  
data | String data payload for this section.  
  
### Description

A names raw data section whose payload is derived from a UTF8 string, with a
default `Content-Type`.

For UTF8 strings, use this constructor. `data` will be assumed to be in UTF8
encoding and converted appropriately. The section will be assigned a `Content-
Type` of `text/plain; encoding=utf8`.

* * *

## Declaration

public MultipartFormDataSection(string data);

### Parameters

data | String data payload for this section.  
---|---  
  
### Description

An anonymous raw data section whose payload is derived from a UTF8 string,
with a default `Content-Type`.

Identical to the above, but without a section name.

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

