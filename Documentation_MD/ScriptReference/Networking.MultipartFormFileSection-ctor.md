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

# MultipartFormFileSection Constructor

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

public MultipartFormFileSection(string name, byte[] data, string fileName,
string contentType);

### Parameters

name | Name of this form section.  
---|---  
data | Raw contents of the file to upload.  
fileName | Name of the file uploaded by this form section.  
contentType | The value for this section's `Content-Type` header.  
  
### Description

Contains a named file section based on the raw bytes from `data`, with a
custom `Content-Type` and file name.

The full-control option. Manually specify a section name, raw data, file name
and `Content-Type`. If `fileName` is null or empty, it defaults to `file.dat`.
If contentType is null or empty, it defaults to `application/octet-stream`.

* * *

## Declaration

public MultipartFormFileSection(byte[] data);

### Parameters

data | Raw contents of the file to upload.  
---|---  
  
### Description

Contains an anonymous file section based on the raw bytes from `data`, assigns
a default `Content-Type` and file name.

Creates a file section based on the raw bytes from the `data` argument.
Assigns a content-type of application/octet-stream and a file name of
file.dat.

* * *

## Declaration

public MultipartFormFileSection(string fileName, byte[] data);

### Parameters

data | Raw contents of the file to upload.  
---|---  
fileName | Name of the file uploaded by this form section.  
  
### Description

Contains an anonymous file section based on the raw bytes from `data` with a
specific file name. Assigns a default `Content-Type`.

Assigns a `Content-Type` of `application/octet-stream`.

* * *

## Declaration

public MultipartFormFileSection(string name, string data, Encoding
dataEncoding, string fileName);

### Parameters

name | Name of this form section.  
---|---  
data | Contents of the file to upload.  
dataEncoding | A string encoding.  
fileName | Name of the file uploaded by this form section.  
  
### Description

Contains a named file section with data drawn from `data`, as marshaled by
`dataEncoding`. Assigns a specific file name from `fileName` and a default
`Content-Type`.

`Content-Type` is assumed to be `text/plain`, with an `encoding` drawn from
`dataEncoding`. If `dataEncoding` is null, defaults to UTF8.

* * *

## Declaration

public MultipartFormFileSection(string data, Encoding dataEncoding, string
fileName);

### Parameters

data | Contents of the file to upload.  
---|---  
dataEncoding | A string encoding.  
fileName | Name of the file uploaded by this form section.  
  
### Description

An anonymous file section with data drawn from `data`, as marshaled by
`dataEncoding`. Assigns a specific file name from `fileName` and a default
`Content-Type`.

As above, but unnamed.

* * *

## Declaration

public MultipartFormFileSection(string data, string fileName);

### Parameters

data | Contents of the file to upload.  
---|---  
fileName | Name of the file uploaded by this form section.  
  
### Description

An anonymous file section with data drawn from the UTF8 string `data`. Assigns
a specific file name from `fileName` and a default `Content-Type`.

Convenience method. Specify file contents via the `data` string and assign a
file name via `fileName`. Assumes the string is encoded in UTF8. Assigns a
`Content-Type` of `text/plain; encoding=utf8`. If `fileName` is null or empty,
assigns a file name of `file.txt`.

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

