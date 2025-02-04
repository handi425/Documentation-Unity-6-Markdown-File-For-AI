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

#  [UnityWebRequest](Networking.UnityWebRequest.html).Post

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

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(string uri, string postData, string contentType);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(Uri uri, string postData, string contentType);

### Parameters

uri | The target URI to which the string will be transmitted.  
---|---  
postData | Form body data. Will be converted to UTF-8 string.  
contentType | Value for the Content-Type header, for example application/json.  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to send string to `uri` via
`POST`.

### Description

Creates a UnityWebRequest configured to send form data to a server via HTTP
`POST`.

This method creates a UnityWebRequest, sets the `url` to the string `uri`
argument and sets the `method` to `POST`. The `Content-Type` header will be
set to `contentType`.  
  
This method attaches a
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html). This is for convenience,
as we anticipate most users will use the
[DownloadHandler](Networking.DownloadHandler.html) to check replies from the
server, particularly in the case of REST APIs.  
  
The data in `postData` will be interpreted into a byte stream via
[System.Text.Encoding.UTF8](https://msdn.microsoft.com/en-
us/library/system.text.encoding.utf8). The resulting byte stream will be
stored in an [UploadHandlerRaw](Networking.UploadHandlerRaw.html) and the
Upload Handler will be attached to this UnityWebRequest.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class MyBehavior : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(Upload());
        }  
      
        IEnumerator Upload()
        {
            using ([UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)("https://www.my-server.com/myapi", "{ \"field1\": 1, \"field2\": 2 }", "application/json"))
            {
                yield return www.SendWebRequest();  
      
                if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
                {
                    [Debug.LogError](Debug.LogError.html)(www.error);
                }
                else
                {
                    [Debug.Log](Debug.Log.html)("Form upload complete!");
                }
            }
        }
    }
    

* * *

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(string uri, [WWWForm](WWWForm.html) formData);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(Uri uri, [WWWForm](WWWForm.html) formData);

### Parameters

uri | The target URI to which form data will be transmitted.  
---|---  
formData | Form fields or files encapsulated in a [WWWForm](WWWForm.html) object, for formatting and transmission to the remote server.  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to send form data to `uri`
via `POST`.

### Description

Create a UnityWebRequest configured to send form data to a server via HTTP
`POST`.

This method creates a UnityWebRequest, sets the `url` to the string `uri`
argument and sets the `method` to `POST`. The `Content-Type` header will be
copied from the `formData` parameter.  
  
This method attaches a
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html). This is for convenience,
as we anticipate most users will use the
[DownloadHandler](Networking.DownloadHandler.html) to check replies from the
server, particularly in the case of REST APIs.  
  
The `formData` object will generate an appropriately-formatted byte stream,
depending on its contents. The resulting byte stream will be stored in an
[UploadHandlerRaw](Networking.UploadHandlerRaw.html) and the Upload Handler
will be attached to this UnityWebRequest.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;  
      
    public class MyBehavior2 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(Upload());
        }  
      
        IEnumerator Upload()
        {
            [WWWForm](WWWForm.html) form = new [WWWForm](WWWForm.html)();
            form.AddField("myField", "myData");  
      
            using [UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)("https://www.my-server.com/myform", form);
            yield return www.SendWebRequest();  
      
            if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                [Debug.LogError](Debug.LogError.html)(www.error);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Form upload complete!");
            }
        }
    }
    

* * *

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(string uri, List<IMultipartFormSection> multipartFormSections);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(Uri uri, List<IMultipartFormSection> multipartFormSections);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(string uri, List<IMultipartFormSection> multipartFormSections, byte[]
boundary);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(Uri uri, List<IMultipartFormSection> multipartFormSections, byte[]
boundary);

### Parameters

uri | The target URI to which form data will be transmitted.  
---|---  
multipartFormSections | A list of form fields or files to be formatted and transmitted to the remote server.  
boundary | A unique boundary string, which will be used when separating form fields in a multipart form. If not supplied, a boundary will be generated for you.  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to send form data to `uri`
via `POST`.

### Description

Create a UnityWebRequest configured to send form data to a server via HTTP
`POST`.

This method creates a UnityWebRequest, sets the `url` to the string `uri`
argument and sets the `method` to `POST`. The `Content-Type` header will be
set to `multipart/form-data`, with an appropriate boundary specification.  
  
If you supply a custom `boundary` byte array, note that the sequence of bytes
must be guaranteed to be unique and must not appear anywhere in the body of
your form data. For more information on multipart forms and form boundaries,
see [RFC 2388](https://www.ietf.org/rfc/rfc2388.txt).  
  
This method attaches a
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html). This is for convenience,
as we anticipate most users will use the
[DownloadHandler](Networking.DownloadHandler.html) to check replies from the
server, particularly in the case of REST APIs.  
  
The List of [IMultipartFormSection](Networking.IMultipartFormSection.html)
objects in `multipartFormSections` will be formatted into a valid multipart
form body. Each object will be interpreted as a discrete form section. The
byte stream resulting from formatting this multipart form body will be stored
in an [UploadHandlerRaw](Networking.UploadHandlerRaw.html) and attached to
this UnityWebRequest.  
  
**Using IMultipartFormSection**  
  
To provide greater control over how you specify your form data, the
UnityWebRequest system contains a (user-implementable)
[IMultipartFormSection](Networking.IMultipartFormSection.html) interface. For
standard applications, Unity also provides default implementations for data
and file sections.  
  
Additional resources:
[MultipartFormDataSection](Networking.MultipartFormDataSection.html) and
[MultipartFormFileSection](Networking.MultipartFormFileSection.html).  
  
A List of IMultipartFormSection objects can be provided to this method. The
list's members will be formatted into a multipart form, as defined by [RFC
2388](https://www.ietf.org/rfc/rfc2388.txt).  
  
Multipart forms require a unique boundary string to define the separation
between fields. The boundary string must be guaranteed to not be present
anywhere within the body of any form field in the request. If you do not
supply a boundary, Unity will generate one. The generated boundary is 40
random printable bytes, which effectively never collide with form field data.
However, if your application requires you to supply a custom boundary string,
you may do so.  
  
The supplied boundary, if any, will be automatically converted from a byte
array to UTF8 characters.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;
    using System.Collections.Generic;  
      
    public class MyBehavior3 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(Upload());
        }  
      
        IEnumerator Upload()
        {
            List<[IMultipartFormSection](Networking.IMultipartFormSection.html)> form = new();
            form.Add(new [MultipartFormDataSection](Networking.MultipartFormDataSection.html)("myField", "myData"));  
      
            using [UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)("https://httpbin.org/post", form);
            yield return www.SendWebRequest();  
      
            if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                [Debug.LogError](Debug.LogError.html)(www.error);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Form upload complete!");
            }
        }
    }
    

* * *

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(string uri, Dictionary<string,string> formFields);

## Declaration

public static [Networking.UnityWebRequest](Networking.UnityWebRequest.html)
Post(Uri uri, Dictionary<string,string> formFields);

### Parameters

uri | The target URI to which form data will be transmitted.  
---|---  
formFields | Strings indicating the keys and values of form fields. Will be automatically formatted into a URL-encoded form body.  
  
### Returns

**UnityWebRequest** A UnityWebRequest configured to send form data to `uri`
via `POST`.

### Description

Create a UnityWebRequest configured to send form data to a server via HTTP
`POST`.

This method creates a UnityWebRequest, sets the `url` to the string `uri`
argument and sets the `method` to `POST`. The `Content-Type` header will be
set to `application/x-www-form-urlencoded`.  
  
The Dictionary of strings in `formFields` will be interpreted as a list of
form fields whose field IDs are the dictionary keys, and whose field values
are the dictionary values. Both keys and values will be escaped, and then
joined into a URL-encoded form string. (for example,
`key1=value1&key2=value2`).  
  
This method, by default, attaches a
[DownloadHandlerBuffer](Networking.DownloadHandlerBuffer.html) to the
[UnityWebRequest](Networking.UnityWebRequest.html). This is for convenience,
as we anticipate most users will use the
[DownloadHandler](Networking.DownloadHandler.html) to check replies from the
server, particularly in the case of REST APIs.  
  
The URL-encoded form string generated from `formFields` will be converted into
a byte stream and stored in an
[UploadHandlerRaw](Networking.UploadHandlerRaw.html), which will be attached
to this UnityWebRequest.

    
    
    using UnityEngine;
    using UnityEngine.Networking;
    using System.Collections;
    using System.Collections.Generic;  
      
    public class MyBehavior4 : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(Upload());
        }  
      
        IEnumerator Upload()
        {
            Dictionary<string, string> form = new();
            form["myField"] = "myData";  
      
            using [UnityWebRequest](Networking.UnityWebRequest.html) www = [UnityWebRequest.Post](Networking.UnityWebRequest.Post.html)("https://httpbin.org/post", form);
            yield return www.SendWebRequest();  
      
            if (www.result != [UnityWebRequest.Result.Success](Networking.UnityWebRequest.Result.Success.html))
            {
                [Debug.LogError](Debug.LogError.html)(www.error);
            }
            else
            {
                [Debug.Log](Debug.Log.html)("Form upload complete!");
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

